from django.urls import path
from . import views

urlpatterns = [
    
    path('de/', views.deep_learning, name='deep'),
    path('register/', views.registration),
]