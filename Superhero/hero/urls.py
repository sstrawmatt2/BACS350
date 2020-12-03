from hero.views import HeroAddView, HeroDetailView, HeroEditView, HeroListView, HeroDeleteView, CardView, TemplateView, HomeView
from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('', HomeView.as_view(template_name='home.html')),
    path('hero_list', HeroListView.as_view(), name='hero_list'),
    path('hero_card', TemplateView.as_view(template_name='hero_card')),
    path('<int:pk>', HeroDetailView.as_view(), name='hero_detail'),
    path('add', HeroAddView.as_view(), name='hero_add'), 
    path('<int:pk>/', HeroEditView.as_view(), name='hero_edit'),
    path('<int:pk>/delete/', HeroDeleteView.as_view(), name='hero_delete'),
    path('', include('accounts.urls')),
    path('', include('workshop.urls')),
    path('', include('blog.urls')),
] 