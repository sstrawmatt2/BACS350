from django.http import HttpResponse
from django.urls import path


def home_page_view(request):
    return HttpResponse("<h1>Hello World!</h1>")

def about_page_view(request):
    return HttpResponse("<h1>ABOUT</h1>")
    


urlpatterns = [
    path('', home_page_view, name='home'),
    path('about', about_page_view),
    
    
]