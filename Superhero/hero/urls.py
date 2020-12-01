from hero.views import HeroAddView, HeroDetailView, HeroEditView, HeroListView, HeroDeleteView, CardView, TemplateView
from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('', HeroListView.as_view(), name='hero_list'),
    path('home', TemplateView.as_view(template_name='home')),
    path('hero_card', TemplateView.as_view(template_name='hero_card')),
    path('markdown', TemplateView.as_view(template_name="markdown.html")),
    path('<int:pk>', HeroDetailView.as_view(), name='hero_detail'),
    path('add', HeroAddView.as_view(), name='hero_add'), 
    path('<int:pk>/', HeroEditView.as_view(), name='hero_edit'),
    path('<int:pk>/delete/', HeroDeleteView.as_view(), name='hero_delete'),
    path('', include('accounts.urls')),
] 