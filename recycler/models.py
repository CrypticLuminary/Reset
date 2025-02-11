from django.db import models

TYPE_OF_RECYCLING = [
    ('plastic','Plastic'),
    ('paper','Paper'),
    ('glass','Glass'),
    ('metal','Metal'),
    ('organic','Organic'),
]

class RecyclingService(models.Model):
    company_name = models.CharField(max_length=100)
    types = models.CharField(choices=TYPE_OF_RECYCLING, max_length=50)
    address = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)

    
