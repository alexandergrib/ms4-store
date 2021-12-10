from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from products.models import Product,Cartridges

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    cartridge = None
    if 'cartridge' in request.POST:
        product = Cartridges.objects.get(pk=item_id)
        cartridge = request.POST['cartridge']
    else:
        product = Product.objects.get(pk=item_id)

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if cartridge:

        if item_id in list(bag.keys()):
            if cartridge in bag[item_id]['cartridge'].keys():
                bag[item_id]['cartridge'][cartridge] += quantity
            else:
                bag[item_id]['cartridge'][cartridge] = quantity
        else:
            bag[item_id] = {'cartridge': {cartridge: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust a quantity of the shopping bag """

    quantity = int(request.POST.get('quantity'))
    cartridge = None
    if 'cartridge' in request.POST:
        cartridge = request.POST['cartridge']
    bag = request.session.get('bag', {})

    if cartridge:
        if quantity > 0:
            bag[item_id]['cartridge'][cartridge] = quantity
        else:
            del bag[item_id]['cartridge'][cartridge]
            if not bag[item_id]['cartridge']:
                bag.pop(item_id)
    else:
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
        cartridge = None
        if 'cartridge' in request.POST:
            size = request.POST['cartridge']
        bag = request.session.get('bag', {})

        if cartridge:
            del bag[item_id]['cartridge'][cartridge]
            if not bag[item_id]['cartridge']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        print(request.session['bag'])
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
