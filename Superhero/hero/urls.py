from django.urls import path

from page.views import AboutView, HomeView, ProfileView

urlpatterns = [
    path('', HeroView.as_view()),
    path('about', AboutView.as_view()),
    path('base', BaseView.as_view()),
    path('<str:identity>', HeroView.as_view()),
]