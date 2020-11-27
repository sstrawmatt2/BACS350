from hero.views import HeroAddView, HeroDetailView, HeroEditView, HeroListView, HeroDeleteView, CardView, TemplateView
from django.urls import path, include


urlpatterns = [
    path('home', TemplateView.as_view(template_name="home.html")),
    path('', HeroListView.as_view(), name='hero_list'),
    path('hero_card', TemplateView.as_view(template_name="hero_card.html")),
    path('markdown', TemplateView.as_view(template_name="markdown.html")),
    path('<int:pk>', HeroDetailView.as_view(), name='hero_detail'),
    path('add', HeroAddView.as_view(), name='hero_add'), 
    path('<int:pk>/', HeroEditView.as_view(), name='hero_edit'),
    path('<int:pk>/', HeroDeleteView.as_view(), name='hero_delete'),
    path('', include('accounts.urls')),
] 