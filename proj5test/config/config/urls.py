from hero.views import HeroAddView, HeroDetailView, HeroEditView, HeroListView, HeroDeleteView
from django.urls import path, include


urlpatterns = [
    path('', HeroListView.as_view(), name='hero_list'),
    path('<int:pk>', HeroDetailView.as_view(), name='hero_detail'),
    path('add', HeroAddView.as_view(), name='hero_add'), 
    path('edit/<int:pk>/', HeroEditView.as_view(), name='hero_add'),
    path('delete/<int:pk>/', HeroDeleteView.as_view(), name='hero_delete'),
    path('', include('accounts.urls')),
]
