from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.conf import settings
import stripe
from kimchis.models import Kimchi
from .models import Purchase
from django.contrib.sites.models import Site
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib import messages


def checkout(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    cart = request.session.get('shopping_cart', {})
    line_items = []
    for kimchi_id, kimchi in cart.items():
        kimchi_model = get_object_or_404(Kimchi, pk=kimchi_id)
        item = {
            "name": kimchi_model.title,
            "amount": int(kimchi_model.price * 100),
            "currency": "sgd",
            "quantity": kimchi['qty'],
            "description": kimchi_model.id
        }
        line_items.append(item)

    current_site = Site.objects.get_current()
    domain = current_site.domain

    # create a session to represent currnet transaction
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],  # take credit cards
        line_items=line_items,
        client_reference_id=request.user.id,
        success_url=domain + reverse(checkout_success),
        cancel_url=domain + reverse(checkout_cancelled)
    )

    return render(request, "checkout/checkout.template.html", {
        "session_id": session.id,
        "public_key": settings.STRIPE_PUBLISHABLE_KEY
    })


def checkout_success(request):
    # empty the shopping cart
    request.session['shopping_cart'] = {}
    messages.success(request, "Your purchase made successfully")
    return redirect(reverse("all_kimchis_route"))


def checkout_cancelled(request):
    return HttpResponse("Checkout cancelled")


@csrf_exempt
def payment_completed(request):
    payload = request.body

    # verify that the payment is legit
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']

    endpoint_secret = "whsec_r6rZghMXywoVVUk1MmAKPisu7F1bC16S"
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret)
    except ValueError:
        # invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        # invalid signature
        return HttpResponse(status=400)

    if event["type"] == "checkout.session.completed":
        # retrieve the session data
        session = event['data']['object']
        handle_payment(session)

    return HttpResponse(status=200)


def handle_payment(session):
    print(session)
    user = get_object_or_404(User, pk=session['client_reference_id'])

    for line_item in session["display_items"]:
        kimchi_id = int(line_item['custom']['description'])
        kimchi_model = get_object_or_404(Kimchi, pk=kimchi_id)

        # create the purchase model
        purchase = Purchase()
        purchase.kimchi_id = kimchi_model
        purchase.user_id = user
        purchase.save()
