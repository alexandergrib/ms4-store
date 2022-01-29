from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from django.http import Http404
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from config import settings
from profiles.models import UserProfile
from .forms import (ProductForm, CategoryForm, BrandForm,
                    ProductSpecsForm, CartrigesForm, RatingForm)
from .models import (Product,
                     Category,
                     Cartridges,
                     ProductBrand,
                     ProductReviews, ProductImages, ProductSpecifications)
from checkout.models import OrderLineItem


def all_products(request):
    """ A view to show all products, including sorting and search queries """
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    reviews = ProductReviews.objects.all()
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('model'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
        if 'brand' in request.GET:
            brands_list = request.GET['brand'].split(',')
            products = Product.objects.all().filter(
                brand__brand_name__in=brands_list)
        if 'special' in request.GET:
            special_list = request.GET['special'].split(',')
            products = Product.objects.all().filter(
                special__name__in=special_list
            )

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query) | Q(
                brand__brand_name__icontains=query
            )
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """
    cartridge_form = CartrigesForm()
    order = OrderLineItem.objects.all()
    reviews = ProductReviews.objects.all()
    try:
        product = get_object_or_404(Product, pk=product_id)
        from_page = 'product'
    except Http404:  # if not product then it's a cartridge
        product = get_object_or_404(Cartridges, pk=product_id)
        from_page = 'cartridge'
    # find if user purchased this product

    if not request.user.id:
        can_rate = False
    else:
        can_rate_query = order.filter(
            order__user_profile__id__icontains=request.user.id
        ).filter(
            product__id=product_id)

        if can_rate_query.exists():
            #user purchased product and can rate
            review_filtered = reviews.filter(
                user__id__icontains=request.user.id).filter(
                product__id__icontains=product_id)
            if review_filtered.exists():
                #  if rated already
                can_rate = False
            else:
                can_rate = True
        else:
            can_rate = False

    context = {
        'product': product,
        'form': cartridge_form,
        'from_page': from_page,
        'can_rate': can_rate
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def all_categories(request):
    categories = Category.objects.all()
    form = CategoryForm()
    context = {
        "categories": categories,
        'form': form
    }
    return render(request, 'products/categories.html', context)


@login_required
def all_brands(request):
    brands = ProductBrand.objects.all()
    form = BrandForm()
    context = {
        "brands": brands,
        'form': form
    }
    return render(request, 'products/brand.html', context)


@login_required
def all_specs(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    specs = ProductSpecifications.objects.filter(product__id__exact=product_id)
    form = ProductSpecsForm()
    context = {
        "specs": specs,
        'form': form,
        'product': product
    }
    return render(request, 'products/all_product_specs.html', context)


def all_reviews(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    reviews = ProductReviews.objects.filter(product__id__exact=product_id)
    context = {
        'product': product,
        'reviews': reviews,
    }
    return render(request, 'products/reviews.html', context)


@login_required
def add_brand(request):
    """Add new product category"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            brand = form.save()
            messages.success(request, 'Successfully added new category!')
            return redirect(reverse('add_product'))
        else:
            messages.error(
                request,
                'Failed to add category. Please ensure the form is valid.')
    else:
        form = BrandForm()

    template = 'products/add_brand.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_category(request):
    """Add new product category"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            messages.success(request, 'Successfully added new category!')
            return redirect(reverse('add_product'))
        else:
            messages.error(
                request,
                'Failed to add category. Please ensure the form is valid.')
    else:
        form = CategoryForm()

    template = 'products/add_category.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.created_by = UserProfile.objects.get(user=request.user)
            product = form.save()
            if form.cleaned_data['images']:
                images = request.FILES.getlist('images')
                for image in images:
                    ProductImages.objects.create(
                        image=image, product=product,
                        image_url=settings.MEDIA_URL + image.name)
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_specs(request, product_id):
    """Add new product category"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductSpecsForm(request.POST)
        if form.is_valid():
            specs = form.save()
            messages.success(request, 'Successfully added new specs!')
            return redirect('product_detail', product_id=product_id)
        else:
            messages.error(
                request,
                'Failed to add specs. Please ensure the form is valid.')
    else:
        form = ProductSpecsForm()

    template = 'products/add_product_specifications.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_cartridge(request, product_id):
    """Add new product category"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = CartrigesForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            user = form.save(commit=False)
            user.created_by = UserProfile.objects.get(user=request.user)
            if form.cleaned_data['image']:
                image = request.FILES.get('image')
                cartridge_form = form.save(commit=False)
                cartridge_form.image_url = settings.MEDIA_URL + image.name
                cartridge_form.save()
            else:
                form.save()
            messages.success(request, 'Successfully added new cartridge!')
            return redirect('product_detail', product_id=product_id)
        else:
            messages.error(
                request,
                'Failed to add cartridge. Please ensure the form is valid.')
    else:
        form = CartrigesForm()

    template = 'products/add_cartridge.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_review(request, product_id):
    """ Add a product review """
    product = get_object_or_404(Product, pk=product_id)
    user = UserProfile.objects.get(user=request.user)
    user_review = ProductReviews.objects.filter(product=product, user=user)
    review_form = RatingForm(request.POST)

    if request.method == 'POST':
        if user_review:
            messages.error(request, "You have reviewed this product already.")
            return redirect(reverse('product_detail', args=[product.id]))

        else:
            if review_form.is_valid():
                # in future review image will be uploaded to S3
                # image field not used at this moment
                review = review_form.save(commit=False)
                review.user = user
                review.product = product
                review.save()
                messages.info(request, 'Thank you for your review!')
                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(request, "Ensure the form is valid. \
                                    Please try again!")

    else:
        review_form = RatingForm(instance=product)

    template = 'products/add_review.html'
    context = {
        'form': review_form,
        'product': product,
    }

    return render(request, template, context)


# ---------------------edit  functions


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product_images = ProductImages.objects.filter(product=product.id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            if form.cleaned_data['images']:
                images = request.FILES.getlist('images')
                for image in images:
                    ProductImages.objects.create(
                        image=image, product=product,
                        image_url=settings.MEDIA_URL + image.name)
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(
            request, f'You are editing \
            {product.brand.friendly_brand_name} \
            {product.model} {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
        'product_images': product_images
    }

    return render(request, template, context)


@login_required
def edit_cartridge(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    cartridge = get_object_or_404(Cartridges, pk=product_id)
    if request.method == 'POST':
        form = CartrigesForm(request.POST, request.FILES, instance=cartridge)
        if form.is_valid():
            user = form.save(commit=False)
            user.created_by = UserProfile.objects.get(user=request.user)
            if form.cleaned_data['image']:
                image = request.FILES.get('image')
                if image:
                    cartridge_form = form.save(commit=False)
                    cartridge_form.image_url = settings.MEDIA_URL + image.name
                    cartridge_form.save()
            else:
                form.save()
    else:
        form = CartrigesForm(instance=cartridge)
        messages.info(request, f'You are editing \
        {cartridge.brand.friendly_brand_name} \
        {cartridge.model} {cartridge.name}')

    template = 'products/edit_cartridge.html'
    context = {
        'form': form,
        'cartridge': cartridge,

    }
    return render(request, template, context)


@login_required
def edit_review(request, review_id):
    """ Save edited product review """
    review = get_object_or_404(ProductReviews, pk=review_id)
    if request.user.is_superuser or request.user == review.user.user:
        if request.method == 'POST':
            review_form = RatingForm(request.POST, instance=review)
            if review_form.is_valid():
                review_form.save()
                messages.info(request, 'Your review has been updated!')
                return redirect(reverse('product_detail',
                                args=[review.product.id]))
            else:
                messages.error(request, 'Failed to update the review. \
                                        Please ensure the form is valid.')
        else:
            review_form = RatingForm(instance=review)

        template = 'products/edit_review.html',
        context = {
            'form': review_form,
            'review': review,
            'product_id': review.product.id
        }
        return render(request, template, context)
    else:
        messages.error(
            request, 'Sorry, only the reviewer can edit this review!')
        return redirect(reverse('product_detail', args=[review.product.id]))


# --------------------Delete functions-------------------


@login_required
def delete_product(request, product_id):
    """ Delete product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def delete_brand(request, brand_id):
    """ Delete Brand from the DB """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    brand = get_object_or_404(ProductBrand, pk=brand_id)
    brand.delete()
    messages.success(request, f'Brand {brand.friendly_brand_name} deleted!')
    return redirect(reverse('all_brands'))


@login_required
def delete_category(request, category_id):
    """ Delete category from the DB """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    category = get_object_or_404(Category, pk=category_id)
    category.delete()
    messages.success(request, f'Category {category.friendly_name} deleted!')
    return redirect(reverse('all_categories'))


@login_required
def delete_image(request, image_id):
    """ Delete image from the DB """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    image = get_object_or_404(ProductImages, pk=image_id)
    image.delete()
    messages.success(request, 'Image deleted!')
    return redirect(reverse('products'))


@login_required
def delete_spec(request, spec_id):
    """ Delete Brand from the DB """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    spec = get_object_or_404(ProductSpecifications, pk=spec_id)
    spec.delete()
    messages.success(request, f'Specification {spec.name} deleted!')
    return redirect('products')


@login_required
def delete_cartridge(request, product_id):
    """ Delete Brand from the DB """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    try:
        cartridge = get_object_or_404(Cartridges, pk=product_id)
    except Http404:
        messages.success(request, f'No cartridge with id {product_id} found')
        return redirect('products')
    cartridge.delete()
    messages.success(request, f'Cartridge {cartridge.model} deleted!')
    return redirect('products')


@login_required
def delete_review(request, review_id):
    """ Delete user's existing review """

    review = get_object_or_404(ProductReviews, pk=review_id)
    if request.user.is_superuser or request.user == review.user.user:
        review.delete()
        messages.info(request, 'Your review has been deleted!')
        return redirect(reverse('products'))
    else:
        messages.error(request, 'Sorry, only the reviewer can do that.')
        return redirect(reverse('products'))
