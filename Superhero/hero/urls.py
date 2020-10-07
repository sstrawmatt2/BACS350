
from hero.views import AboutPage, BasePage, HeroView, BatmanView, CapView, BartonView, HulkView, HomeView, DeadshotView
from django.urls import path

urlpatterns = [
    path('', HeroView.as_view()),
    path('home', HomeView.as_view(), name='home'),
    path('about', AboutPage.as_view()),
    path('base', BasePage.as_view()),
    path('<str:identity>', HeroView.as_view()),
    path('batman', BatmanView.as_view(), name='batman'),
    path('cap', CapView.as_view(), name='cap'),
    path('barton', BartonView.as_view(), name='barton'),
    path('hulk', HulkView.as_view(), name='hulk'),
    path('deadshot', DeadshotView.as_view(), name='deadshot'),
    
]
