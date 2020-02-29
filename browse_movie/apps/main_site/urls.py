from django.urls import path

from .views import home_page, ajax_search


urlpatterns = [
    path('', home_page, name="home_page"),
    path('ajax-search/', ajax_search),
]
