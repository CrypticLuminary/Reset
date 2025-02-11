from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from views import *

urlpatterns = [
    path('wastepost/', wastepost, name='wastepost'),
    path('post_list/', post_list, name='post_list'),
]

# Append media URL patterns for development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)