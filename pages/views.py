from django.shortcuts import render
from django.views.generic import DetailView, View, TemplateView

# Create your views here.
class Home(TemplateView):
    template_name="pages/home.html"
    
class About(TemplateView):
    template_name="pages/about.html"
    
class Services(TemplateView):
    template_name="pages/services.html"
    
class Contacts(TemplateView):
    template_name="pages/contact.html"
    