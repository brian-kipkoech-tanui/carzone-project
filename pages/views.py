from django.shortcuts import render
from django.views.generic import DetailView, View, TemplateView
from . models import Team
from cars.models import Car

# Create your views here.
class Home(TemplateView):
    template_name="pages/home.html"
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['teams'] = Team.objects.all()
        context['featured_cars'] = Car.objects.order_by('-created_date').filter(is_featured=True)
        context['all_cars'] = Car.objects.all().order_by('-created_date')
        # context['search_fields'] = Car.objects.values('color', 'city', 'state', 'year', 'body_style')
        context['color_search'] = Car.objects.values_list('color', flat=True).distinct()
        context['city_search'] = Car.objects.values_list('city', flat=True).distinct()
        context['year_search'] = Car.objects.values_list('year', flat=True).distinct()
        context['body_style_search'] = Car.objects.values_list('body_style', flat=True).distinct()
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
    