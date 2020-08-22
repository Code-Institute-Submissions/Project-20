from django.urls import path
import reviews.views


urlpatterns = [
    path('all/', reviews.views.all_reviews,
         name="all_reviews_route"),
    path('create/', reviews.views.create_review,
         name="create_review_route"),
    path('details/<review_id>', reviews.views.review_details,
         name="review_details_route"),
    path('update/<review_id>', reviews.views.update_review,
         name="update_review_route"),
    path('delete/<review_id>', reviews.views.delete_review,
         name="delete_review_route"),
    path('comment/create/<review_id> ', reviews.views.create_comment,
         name="create_comment_route"),
]