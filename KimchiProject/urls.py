from django.contrib import admin
from django.urls import path
import kimchis.views
import reviews.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', kimchis.views.index),
    path('reviews/', reviews.views.index)
]
