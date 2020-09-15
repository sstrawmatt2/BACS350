from django.views.generic import TemplateView

# Create your views here.
class HulkView(TemplateView):
    template_name = "hulk.html"
    
    def get_context_data(self, **kwargs):
        return {'title': 'hulk'}
    
class WidowView(TemplateView):
    template_name = "black_widow.html"
    
    def get_context_data(self, **kwargs):
        return {'title': 'black_widow'}
    
     