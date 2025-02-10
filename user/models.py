from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

USER_TYPES_CHOICES = [
    ('producer', 'Waste Producer'),
    ('recycler', 'Recycler'),
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='', blank=True, null=True)
    user_type = models.CharField(max_length=50, choices=USER_TYPES_CHOICES, default='producer')
    contact_info = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    organization_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):  
        return f"{self.user.username}-{self.user_type}"
    
    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'userprofile'):  
        instance.userprofile.save()