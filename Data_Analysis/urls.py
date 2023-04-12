from django.urls import path
from . import views

urlpatterns = [
    
    path('dataA/', views.data_analysis, name='data'),
    path('class/', views.DataAnalysis.as_view()),
]