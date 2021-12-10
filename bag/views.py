from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from products.models import Product,Cartridges

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    try:
        product = get_object_or_404(Product, pk=item_id)
    except Http404:  # if not product then it's a cartridge
        product = get_object_or_404(Cartridges, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Added {product.name} to your bag')
    else:
        bag[item_id] = quantity
        messages.error(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust a quantity of the shopping bag """

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove an item from the shopping bag """
    try:
        bag = request.session.get('bag', {})
        bag.pop(item_id)

        request.session['bag'] = bag
        print(request.session['bag'])
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)