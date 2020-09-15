from django.views.generic import TemplateView

# Create your views here.
class HulkView(TemplateView):
    template_name = "hulk.html"
    
class WidowView(TemplateView):
    template_name = "black_widow.html"