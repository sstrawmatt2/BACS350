from django.urls import path
from django.views.generic import AboutView, HomeView

urlpatterns = [
    path('about', AboutView.as_view()),
    path('home', HomeSView.as_view()),
    path('', TemplateView.as_view()),
]
