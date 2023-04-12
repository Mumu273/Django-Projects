from django.urls import path
from . import views

urlpatterns = [
     path('bl/', views.blog1, name='blog'),
     path('fm/', views.showformsdata)
]