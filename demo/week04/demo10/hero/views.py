
from django.views.generic import TemplateView


class HeroView(TemplateView):
    template_name = "hero.html"

    def get_context_data(self, **kwargs):
        id = kwargs.get('identity')
        return {'hero': id}
#    this asks for a key_word_argument(kwargs), which is the identity and then it returns it. If there is no identity then the default could be set to hulk or something like that. 

class BasePage(TemplateView):
    template_name = "page_theme.html"
    
class AboutPage(TemplateView):
    template_name = "about.html"