from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from kimchis.models import Kimchi


@login_required
def add_to_cart(request, kimchi_id):
    cart = request.session.get('shopping_cart', {})

    if kimchi_id not in cart:
        kimchi_to_be_added = get_object_or_404(Kimchi, pk=kimchi_id)

        cart[kimchi_id] = {
            'id': kimchi_id,
            'name': kimchi_to_be_added.title,
            'price': float(kimchi_to_be_added.price),
            'qty': 1,
            'total_price': float(kimchi_to_be_added.price)
        }
        messages.success(
            request, f"'{kimchi_to_be_added.title}' added to your cart")

    else:
        cart[kimchi_id]['qty'] += 1

    # save the shopping cart back to the session
    request.session['shopping_cart'] = cart
    return redirect(reverse('view_cart_route'))


@login_required
def view_cart(request):
    cart = request.session.get('shopping_cart', {})

    total = 0
    for k, v in cart.items():
        total += float(v['price']) * int(v['qty'])

    return render(request, 'cart/view_cart.template.html', {
        'cart': cart,
        'total': total
    })


@login_required
def remove_from_cart(request, kimchi_id):
    cart = request.session['shopping_cart']

    if kimchi_id in cart:
        del cart[kimchi_id]

        # save back the shopping cart into the session
        request.session['shopping_cart'] = cart

    messages.success(request, "The item removed succesfully")
    return redirect(reverse('view_cart_route'))


@login_required
def update_quantity(request, kimchi_id):
    cart = request.session['shopping_cart']

    if kimchi_id in cart:
        cart[kimchi_id]['qty'] = request.POST['qty']
        cart[kimchi_id]['total_price'] = int(
            request.POST['qty']) * float(cart[kimchi_id]['price'])
        request.session['shopping_cart'] = cart
        messages.success(
            request, "Quantity updated succesfully")
        return redirect(reverse('view_cart_route'))
    else:
        messages.success(request, "Kimchi does not exitst in your cart")
        return redirect(reverse('view_cart_route'))
