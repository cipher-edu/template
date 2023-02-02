from django.urls import path
from .views import *
urlpatterns = [
    path('',home, name='home'  ),
    path('archive/', blog, name='blog'),
    path('category/', cat, name='category')
]
