from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hero.urls')),
    path('', include('accounts.urls')),
    path('workshop/', include('workshop.urls')),
    path('post_list/', include('blog.urls')),
] 

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)