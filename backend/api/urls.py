from django.urls import path
from .views import upload_csv, equipment_list

urlpatterns = [
    path('upload/', upload_csv),
    path('equipment/', equipment_list),
]

