from django.contrib import admin
from django.urls import path
import kimchis.views
import reviews.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', kimchis.views.home,
         name="home_route"),
    path('kimchis/all', kimchis.views.all_kimchis,
         name="all_kimchis_route"),
    path('reviews/all', reviews.views.all_reviews,
         name="all_reviews_route"),
    path('reviews/create', reviews.views.create_review),
    path('reviews/details/<review_id>', reviews.views.review_details,
         name="review_details_route"),
    path('reviews/update/<review_id>', reviews.views.update_review,
         name="update_review_route")

]
