from django.urls import path
from .views import justview

urlpatterns = [
    path('', justview, name='home'), 
]
