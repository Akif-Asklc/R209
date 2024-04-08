from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('index/', views.index),
    path('seconde/', views.seconde),
    path('formulaire/', views.formulaire),
]
