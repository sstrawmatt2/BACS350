from django.urls import path

from workshop.views import HomeView

urlpatterns = [
    path('', HomeView.as_view()),
    
]
