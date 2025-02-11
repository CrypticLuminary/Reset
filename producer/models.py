from django.db import models
from django.contrib.auth.models import User

# TYPESOFORGANIZATION = [
#     ('construction', 'Construction and Infrastructure'),
#     ('hospitality', 'Hospitality and Food Services'),
#     ('manufacturing', 'Manufacturing and Production'),
#     ('agriculture', 'Agriculture and Farming'),
#     ('healthcare', 'Healthcare and Medical Services'),
#     ('education', 'Education and Training'),
#     ('retail', 'Retail and Wholesales'),
#     ('transportation', 'Transportation and Automotive'),
#     ('electronics', 'Electronics and Technology'),
#     ('chemical', 'Chemical'),
#     ('pharmaceutical', 'Pharmaceutical'),
# ]

# class ProducerInfo(models.Model):  
#     producerName = models.CharField(max_length=100)
#     typeOforganization = models.CharField(
#         max_length=50,  
#         choices=TYPESOFORGANIZATION
#     )
#     location = models.CharField(max_length=100)
#     contact = models.CharField(max_length=100)
class PostWasteDetails(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=100)
    image = models.ImageField(upload_to='media/wasteimages')
    category = models.CharField(max_length=50, default='Uncategorized')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.description} by {self.name.username}"
