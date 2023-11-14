from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):

    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is nothing in your shopping bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OCQaYAzZE8l2RlxWpA1vHMDDGQalZMTZTaksxhLyNqYrxAY8SDSk2rEJxBLgWjaUp2pSgLUnBtDU3dFFeE4Mh8600H4yekNoH',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)
