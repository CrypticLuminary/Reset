from django.db import models

TYPESOFORGANIZATION = [
    ('construction', 'Construction and Infrastructure'),
    ('hospitality', 'Hospitality and Food Services'),
    ('manufacturing', 'Manufacturing and Production'),
    ('agriculture', 'Agriculture and Farming'),
    ('healthcare', 'Healthcare and Medical Services'),
    ('education', 'Education and Training'),
    ('retail', 'Retail and Wholesales'),
    ('transportation', 'Transportation and Automotive'),
    ('electronics', 'Electronics and Technology'),
    ('chemical', 'Chemical'),
    ('pharmaceutical', 'Pharmaceutical'),
]

class ProducerInfo(models.Model):  
    producerName = models.CharField(max_length=100)
    typeOforganization = models.CharField(
        max_length=50,  
        choices=TYPESOFORGANIZATION
    )
    location = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)