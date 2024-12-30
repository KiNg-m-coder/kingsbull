from django.contrib import admin
from django.urls import path, include
from social.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('social/', include('social.urls')),
    path('shop/', include('shop.urls')),
    path('games/', include('games.urls')),
    path('', home, name='home'),
]
