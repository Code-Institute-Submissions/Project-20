from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.contrib import messages
from kimchis.models import Kimchi

 
def add_to_cart(request, kimchi_id):
    cart = request.session.get('shopping_cart', {})

    if kimchi_id not in cart:
        kimchi_to_be_added = get_object_or_404(Kimchi, pk=kimchi_id)

        cart[kimchi_id] = {
            'id': kimchi_id,
            'name': kimchi_to_be_added.title,
            'price': 99,
            'qty': 1
        }
    else:
        cart[kimchi_id]['qty'] += 1

    # save the shopping cart back to the session
    request.session['shopping_cart'] = cart

    print(request.session['shopping_cart'])
    return HttpResponse("Kimchi added")


def view_cart(request):
    cart = request.session['shopping_cart']
    return render(request, 'cart/view_cart.template.html', {
        'cart': cart
    })

