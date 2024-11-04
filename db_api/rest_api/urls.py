from django.urls import path
from .views import get_quantity_view, get_record_by_id_view


urlpatterns = [
    path('quantity/', get_quantity_view),
    path('by_id/id=<int:id>', get_record_by_id_view)
]
