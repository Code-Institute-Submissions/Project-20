from django.urls import path
import kimchis.views


urlpatterns = [
    path('all/', kimchis.views.all_kimchis,
         name="all_kimchis_route"),
    path('details/<kimchi_id>', kimchis.views.kimchi_details,
         name="kimchi_details_route")
]