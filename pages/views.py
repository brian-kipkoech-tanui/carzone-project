from django.shortcuts import render
from django.views.generic import DetailView, View, TemplateView

# Create your views here.
class Home(TemplateView):
    template_name="home.html"