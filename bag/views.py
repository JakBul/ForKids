from django.shortcuts import render, redirect, reverse, HttpResponse


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    # while in the session, find the bag or create one
    bag = request.session.get('bag', {})

    # add item into the bag or update the quantity if it already exists
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    # overwrite the variable with the updated version
    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust the quantity of the specified product to the specified amount """

    quantity = int(request.POST.get('quantity'))

    # while in the session, find the bag or create one
    bag = request.session.get('bag', {})

    # adjust the quantity
    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    # overwrite the variable with the updated version
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

def remove_from_bag(request, item_id):
    """ Remove the item from the shopping bag """
    
    try:
        # while in the session, find the bag or create one
        bag = request.session.get('bag', {})

        bag.pop(item_id)

        # overwrite the variable with the updated version
        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
