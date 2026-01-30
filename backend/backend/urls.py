from django.contrib import admin
from django.urls import path, include   # 👈 include add pannunga
from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to Chemical Equipment Visualizer API!")


urlpatterns = [
    path('', home),  # root URL
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # api urls include pannra
]

