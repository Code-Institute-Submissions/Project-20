from django.urls import path
import website.views


urlpatterns = [
    path('', website.views.home, name="home_route")
]