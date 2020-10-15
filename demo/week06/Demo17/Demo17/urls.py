
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView


class HeroView(TemplateView):
    template_name="hero.html"
    
    
    
urlpatterns = [
    path('', TemplateView.as_view()),
]
