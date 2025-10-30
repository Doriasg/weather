from django.urls import path, include
from site_meteo import views

urlpatterns = [
    path('predict/', views.weather_predict, name='weather_predict'),
    path('', views.home, name='home'),
]

