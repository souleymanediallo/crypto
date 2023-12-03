from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('price/', views.price, name='price'),
    path('search/', views.search, name='search'),
]
