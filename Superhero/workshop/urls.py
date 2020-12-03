from django.urls import path, include

from workshop.views import CardView, CardsView, HomeView


urlpatterns = [
    
    path('',  HomeView.as_view(), name='workshop'),
    
    path('card',  CardView.as_view(), name='card'),
    path('cards',  CardsView.as_view(), name='cards'),
    
]