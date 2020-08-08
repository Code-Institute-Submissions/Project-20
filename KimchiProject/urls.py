from django.contrib import admin
from django.urls import path
import kimchis.views
import reviews.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', kimchis.views.home,
         name="home_route"),
    path('kimchis/all', kimchis.views.all_kimchis),
    path('reviews/all', reviews.views.all_reviews)
]
