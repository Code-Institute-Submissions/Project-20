from django.contrib import admin
from django.urls import path, include
import kimchis.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', kimchis.views.home,
         name="home_route"),
    path('kimchis/', include('kimchis.urls')),
    path('reviews/', include('reviews.urls')),
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls'))
]
