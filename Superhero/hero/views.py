
from django.views.generic import TemplateView

from hero.models import Superhero

class HeroView(TemplateView):
    template_name="hero.html"
    
    def get_context_data(self, **kwargs):
        heroes = Superhero.objects.all()
        return{'heroes': heroes, 'css': '/static/hero.css'}
    
#    def get_context_data(self, **kwargs):
#        heroes = Superhero.objects.all()
#        return {
#            'title': 'Superhero Profile',
#            'heroes': heroes, 
#        }
    



class HomePage(TemplateView):
    template_name = "home.html"
    
class AboutPage(TemplateView):
    template_name = "about.html"

    
    
    
    
#
#class HeroView(TemplateView):
#    template_name = "hero.html"
#
#    def get_context_data(self, **kwargs):
#        id = kwargs.get('identity', 'Hero')
#        return {'hero': id, 'css': '/static/hero.css'}
#
#class BasePage(TemplateView):
#    template_name = "page_theme.html"
#
#class HomePage(TemplateView):
#    template_name = "home.html"
#    
#class AboutPage(TemplateView):
#    template_name = "about.html"
#    
#class BatmanView(TemplateView):
#    template_name = "batman.html"
#
#class CapView(TemplateView):
#    template_name = "cap.html"
#    
#class BartonView(TemplateView):
#    template_name = "barton.html"
#
#class HulkView(TemplateView):
#    template_name = "hulk.html"
#    
#class DeadshotView(TemplateView):
#    template_name = "deadshot.html"



