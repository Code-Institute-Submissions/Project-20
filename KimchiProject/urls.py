from django.contrib import admin
from django.urls import path, include
import kimchis.views
import reviews.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('home/', kimchis.views.home,
         name="home_route"),
    path('kimchis/all', kimchis.views.all_kimchis,
         name="all_kimchis_route"),
    path('kimchis/details/<kimchi_id>', kimchis.views.kimchi_details,
         name="kimchi_details_route"),
    path('reviews/all', reviews.views.all_reviews,
         name="all_reviews_route"),
    path('reviews/create', reviews.views.create_review,
         name="create_review_route"),
    path('reviews/details/<review_id>', reviews.views.review_details,
         name="review_details_route"),
    path('reviews/update/<review_id>', reviews.views.update_review,
         name="update_review_route"),
    path('reviews/delete/<review_id>', reviews.views.delete_review,
         name="delete_review_route"),
    path('reviews/create/comment/<review_id> ', reviews.views.create_comment,
         name="create_comment_route"),

]
