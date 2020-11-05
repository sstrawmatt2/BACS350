
from django.views.generic import DetailView, ListView,TemplateView
from django.views.generic.edit import CreateView, UpdateView 
from hero.models import Superhero
from os.path import exists

     
        
class HeroAddView(CreateView):
    template_name = "hero_add.html"
    model = Superhero 
    fields = '__all__'
    
class HeroDetailView(DetailView):
    template_name = "hero_detail.html"
    model = Superhero  
    
    #This method is responsible for checking if there is an image. If there is not an image,
    #then the user icon will display where the image is at. 
    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        image = kwargs['object'].image
        if not exists('static/' + image):
            kwargs['missing'] = True
        return kwargs
    
#    This method will only work for a few images. It works for 2 heroes
#    then throws up an error about get context data. It has an issue with
#    what is going on in line 21. 
    
        

    
class HeroEditView(UpdateView):
    template_name = "hero_add.html"
    model = Superhero
    fields = '__all__'   
    
    def get_context_data2(self, **kwargs):
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
#   
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
