from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    # use products for messages
    product = get_object_or_404(Product, pk=item_id)

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    # while in the session, find the bag or create one
    bag = request.session.get('bag', {})

    # add item into the bag or update the quantity if it already exists
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(
            request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your shopping bag.')

    # overwrite the variable with the updated version
    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust quantity of the specified product to the specified amount """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))

    # while in the session, find the bag or create one
    bag = request.session.get('bag', {})

    # adjust the quantity
    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(
            request, f'Product {product.name} has been removed from your shopping bag.')

    # overwrite the variable with the updated version
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove the item from the shopping bag """

    try:
        product = get_object_or_404(Product, pk=item_id)
        # while in the session, find the bag or create one
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(
            request, f'Product {product.name} has been removed from your shopping bag.')

        # overwrite the variable with the updated version
        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
