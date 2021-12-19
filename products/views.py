from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from django.http import Http404
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from config import settings
from profiles.models import UserProfile
from .forms import ProductForm, CategoryForm, BrandForm
from .models import (Product,
                     Category,
                     Cartridges,
                     ProductBrand,
                     ProductReviews, ProductImages)


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
                products = products.annotate(lower_name=Lower('name'))
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
    try:
        product = get_object_or_404(Product, pk=product_id)
    except Http404:  # if not product then it's a cartridge
        product = get_object_or_404(Cartridges, pk=product_id)
    context = {
        'product': product,
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
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
        'product_images': product_images
    }

    return render(request, template, context)


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
