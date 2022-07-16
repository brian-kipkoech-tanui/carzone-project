from django.urls import path, include
from . import views

app_name='cars_app'
urlpatterns = [
    path('cars/', views.Cars.as_view(), name="cars"),
]