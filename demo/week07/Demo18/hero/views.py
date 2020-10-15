from django.views.generic import TemplateView

class HeroView(TemplateView):
    template_name="hero.html"
    
    def get_context_data(self, **kwargs):
        return {
            'title': 'Superheroe Profile',
            'name': 'Batman', 
            'identity': 'Bruce Wayne',
            
        }
