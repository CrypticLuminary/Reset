from django.urls import path
from .import views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('complete_profile/',views.complete_profile,name='complete_profile'),
]