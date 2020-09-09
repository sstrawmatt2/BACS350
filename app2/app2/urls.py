
from django.urls import path

from pages.views import AboutView, HomeView

#class HomeView(TemplateView):
#    template_name='home.html'

urlpatterns = [
    path('home', HomeView.as_view()),
    path('about', AboutView.as_view()),
]