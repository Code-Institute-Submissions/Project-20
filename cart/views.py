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
            'price': float(kimchi_to_be_added.price),
            'qty': 1
        }
        messages.success(request, f"Added '{kimchi_to_be_added.title}' to the shopping cart")

    else:
        cart[kimchi_id]['qty'] += 1

    # save the shopping cart back to the session
    request.session['shopping_cart'] = cart

    print(request.session['shopping_cart'])
    return redirect(reverse('view_cart_route'))


def view_cart(request):
    cart = request.session['shopping_cart']

    total = 0
    for k, v in cart.items():
        total += float(v['price'])

    return render(request, 'cart/view_cart.template.html', {
        'cart': cart,
        'total': total
    })


def remove_from_cart(request, kimchi_id):
    cart = request.session['shopping_cart']

    if kimchi_id in cart:
        del cart[kimchi_id]

        # save back the shopping cart into the session
        request.session['shopping_cart'] = cart

        messages.success(request, "The item removed succesfully")
    return redirect(reverse('view_cart_route'))
