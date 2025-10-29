from django.urls import path, include
from site_meteo import views

urlpatterns = [
    path('', views.home, name='home'),
]

