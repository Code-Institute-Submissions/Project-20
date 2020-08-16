from django.urls import path

import checkout.views


urlpatterns = [
    path('', checkout.views.checkout, name="checkout_route"),
    path('success', checkout.views.checkout_success),
    path('cancelled', checkout.views.checkout_cancelled),
    path('payment_completed', checkout.views.payment_completed)
]
