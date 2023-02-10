from django.urls import path, include
from . import views

app_name='cars_app'
urlpatterns = [
    path('', views.cars, name="cars"),
    path('<int:pk>', views.CarDetail.as_view(), name='car_detail'),
    path('search', views.Search.as_view(), name="search"),
]