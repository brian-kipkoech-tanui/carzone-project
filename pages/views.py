from django.shortcuts import render
from django.views.generic import DetailView, View, TemplateView
from . models import Team

# Create your views here.
class Home(TemplateView):
    template_name="pages/home.html"
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['teams'] = Team.objects.all()
        return context
    
class About(TemplateView):
    template_name="pages/about.html"
    def get_context_data(self, **kwargs):
        # Cal the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["teams"] = Team.objects.all()
        return context
        
    
class Services(TemplateView):
    template_name="pages/services.html"
    
class Contacts(TemplateView):
    template_name="pages/contact.html"
    