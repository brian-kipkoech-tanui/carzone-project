from django.urls import path, include
from . import views

app_name='pages'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about', views.About.as_view(), name="about"),
    path('services', views.Services.as_view(), name="services"),
    path('contact', views.Contacts.as_view(), name="contacts"),
]