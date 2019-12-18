from django.urls import path

from . import views

urlpatterns = [
    path('', views.redirect, name='redirect'),
    path('home/', views.posts, name='posts'),
    path('register/', views.register, name='register'),
    path('makepost/', views.makepost, name='makepost')
]