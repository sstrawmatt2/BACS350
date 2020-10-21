from django.views.generic import DetailView, ListView,TemplateView
from django.views.generic.edit import CreateView, UpdateView
from hero.models import Superhero

     
        
class HeroAddView(CreateView):
    template_name = "hero_add.html"
    model = Superhero 
    fields = '__all__'
    
class HeroDetailView(DetailView):
    template_name = "hero_detail.html"
    model = Superhero  
    
class HeroEditView(UpdateView):
    template_name = "hero_add.html"
    model = Superhero
    fields = '__all__'
    
    def get_context_data(self, **kwargs):
        kwargs = super(HeroEditView, self).get_context_data(**kwargs)
        kwargs['edit'] = True
        return kwargs

class HeroListView(ListView):
    template_name = "hero_list.html"
    model = Superhero
    
    
    
    
    
    
    
#class HeroView(TemplateView):
##    template_name="hero.html"
#    template_name="hero.html"
#    
#    def get_context_data(self, **kwargs):
#        heroes = Superhero.objects.all()
#        return{'heroes': heroes, 'css': '/static/hero.css'}
#    
#        error was thrown on server saying "Superhero matching query does not exist" when I use the hero_detail.html

#        heroes = Superhero.objects.get(pk=1)
#        return{'hero': heroes}           
#class HomePage(TemplateView):
#    template_name = "home.html"
#    
#class AboutPage(TemplateView):
#    template_name = "about.html"

    
  



    
    
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


#    def get_context_data(self, **kwargs):
#        heroes = Superhero.objects.all()
#        return {
#            'title': 'Superhero Profile',
#            'heroes': heroes, 
#        }
