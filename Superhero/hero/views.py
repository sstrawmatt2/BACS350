from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, ListView,TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from hero.models import Superhero
from os.path import exists

     
        
class HeroAddView(LoginRequiredMixin, CreateView):
    template_name = "hero_add.html"
    model = Superhero 
    fields = '__all__'
    
    def form_validation(self, form):
        form.instance.author_id = self.request.user.pk
        return super().form_valid(form)
    
class HeroDetailView(DetailView):
    template_name = "hero_detail.html"
    model = Superhero  
    
    #This method is responsible for checking if there is an image. If there is not an image,
    #then the user icon will display where the image is at. 
    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        image = kwargs['object'].image
        image = f'static/images/{image}.jpg'
        if not exists(image):
            kwargs['missing'] = True
        kwargs['image'] = image
        return kwargs
        

    
class HeroEditView(UpdateView):
    template_name = "hero_edit.html"
    model = Superhero
    fields = '__all__'   
    
#    def get_context_data2(self, **kwargs):
#        kwargs = super(HeroEditView, self).get_context_data(**kwargs)
#        kwargs['edit'] = True
#        return kwargs

class HeroListView(ListView):
    template_name = "hero_list.html"
    model = Superhero
    
    

    

    
    
    
    
    

