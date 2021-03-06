from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("browse_movie.apps.main_site.urls")),
    path('accounts/', include('allauth.urls')),
]
