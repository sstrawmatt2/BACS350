
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView


class HeroView(TemplateView):
    template_name="hero.html"
    
    def get_context_data(self, **kwargs):
        return {
            'title': 'My Hero View', 
            'body': 'Heroes are awesome!',
        }
    
    
urlpatterns = [
    path('', TemplateView.as_view()),
]
