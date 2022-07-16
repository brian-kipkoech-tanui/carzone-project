from django.shortcuts import render
from django.views.generic import DetailView, View, TemplateView

# Create your views here.
class Cars(TemplateView):
    template_name="cars/cars.html"