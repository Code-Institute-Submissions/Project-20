from django.urls import path

import checkout.views


urlpatterns = [
    path('', checkout.views.checkout),
    path('success', checkout.views.checkout_success),
    path('cancelled', checkout.views.checkout_cancelled)
]
