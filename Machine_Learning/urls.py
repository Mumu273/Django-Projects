from django.urls import path
from . import views

urlpatterns = [
    
    path('machine/', views.machine_learning, name='ml'),
    path('rn/', views.random, name='rn'),
    path('knn/', views.K_nearest, name='knn'),
    path('dtree/', views.dtree, name='dt'),
]