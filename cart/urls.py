from django.urls import path
import cart.views


urlpatterns = [
    path('add/<kimchi_id>', cart.views.add_to_cart, name="add_to_cart_route"),
    # path('view/', cart.views.view_cart, name="view_cart_route")
]
