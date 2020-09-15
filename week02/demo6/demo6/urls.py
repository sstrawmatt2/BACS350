from django.urls import path

from page.views import AboutView, HeroView, ProfileView

urlpatterns = [
    path('about', AboutView.as_view()),
    path('hero', HeroView.as_view()),
    path('profile', ProfileView.as_view()),
    path('', HeroView.as_view()),
]
