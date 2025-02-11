from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),  # URL for the signup page
    path('signin/', views.signin, name='signin'),  # URL for the signin page
    path('logout/', views.user_logout, name='logout'),  # URL for the logout page
    path('profile/update/', views.update_profile, name='update_profile'),  # Profile update URL
    # other URLs...
]
