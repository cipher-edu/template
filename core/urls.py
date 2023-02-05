from django.urls import path
from .views import *
urlpatterns = [
    path('',home, name='home'  ),
    path('archive/', blog, name='blog'),
    path('category/', cat, name='category'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('cats/<int:cat_id>/', categories, name='categories'),
]
