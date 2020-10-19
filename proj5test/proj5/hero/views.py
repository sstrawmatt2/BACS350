from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from hero.models import Superhero

class HeroView(TemplateView):
    template_name="hero.html"
    
#    def get_context_data(self, **kwargs):
#        heroes = Superhero.objects.all()
#        return {
#            'title': 'Superhero Profile',
#            'heroes': heroes, 
#        }
    
    def get_context_data(self, **kwargs):
        heroes = Superhero.objects.all()
#        heroes = ['hulk', 'cap']
        return{'heroes': heroes, 'css': '/static/hero.css'}
      

class AddHeroView(CreateView):
    template_name = "hero_add.html"
    model = Superhero
    
    
class BasePage(TemplateView):
    template_name = "page_theme.html"
    
    
class AboutPage(TemplateView):
    template_name = "about.html"