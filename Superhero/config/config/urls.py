from django.urls import path
from hero.views import HeroAddView, HeroDetailView, HeroEditView, HeroListView 
#from hero.views import HeroView, HomePage, AboutPage 

#This code is for proj6,7
urlpatterns = [
#    path('', HeroView.as_view()),
#    path('<str:identity>', HeroView.as_view()),
#    path('home', HomePage.as_view(), name='home'),
#    path('about', AboutPage.as_view(), name = 'about'),
    path('', HeroListView.as_view(), name='hero_list'),
    path('<int:pk>', HeroDetailView.as_view(), name='hero_detail'),
    path('add', HeroAddView.as_view(), name='hero_add'), 
    path('<int:pk>/', HeroEditView.as_view(), name='hero_edit'),
    path('<int:pk>/', HeroDeleteView.as_view(), name='hero_delete'),
]
