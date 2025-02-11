from django.db import models
from django.conf import settings

TYPESOFWASTEPRODUCED = [
    ('construction_and_demolition', 'Construction and Demolition'),
    ('organic', 'Organic'),
    ('plastic', 'Plastic'),
    ('paper_and_cardboard', 'Paper and Cardboard'),
    ('metal', 'Metal'),
    ('glass', 'Glass'),
    ('textile_and_fabric', 'Textile and Fabric'),
    ('electronic', 'Electronic'),
    ('medical', 'Medical'),
    ('chemical', 'Chemical'),
    ('automotive', 'Automotive'),
    ('mixed', 'Mixed'),
    ('agricultural', 'Agricultural'),
    ('biomedical', 'Biomedical'),
]

class FrequencyType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    is_custom = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @classmethod
    def create_default_frequencies(cls):
        defaults = ['Daily', 'Weekly', 'Monthly']
        for freq in defaults:
            cls.objects.get_or_create(name=freq, is_custom=False)

class DisposalMethod(models.Model):
    method_name = models.CharField(max_length=50, unique=True)
    is_custom = models.BooleanField(default=False)

    def __str__(self):
        return self.method_name
    
    @classmethod
    def create_default_disposal_method(cls):
        defaults = ['Landfill', 'Incineration', 'Informal_dumping']
        for method in defaults:
            cls.objects.get_or_create(method_name=method, is_custom=False)

class WasteDetails(models.Model):
    producer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='', blank=True, null=True)
    types_of_waste = models.CharField(max_length=100, choices=TYPESOFWASTEPRODUCED)
    frequency = models.ForeignKey(FrequencyType, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    disposal_method = models.ForeignKey(DisposalMethod, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.producer.username} - {self.types_of_waste}"

    class Meta:
        verbose_name = "Waste Detail"
        verbose_name_plural = "Waste Details"