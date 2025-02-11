from django.urls import path
from .views import *

urlpatterns = [
    path('', justview, name='home'), 
    path('bio/',bioview, name='bio'),
    path('paper/',paperview, name='paper'),
    path('plastic/',plasticview, name='plastic'),
    path('factory/',factoryview, name='factory'),
    path('yard/',yardview, name='yard'),
    path('medical/',medicalview, name='medical'),   
]
