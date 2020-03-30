from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Register(models.Model):
    petition = models.CharField(max_length=999, blank=False)
    email = models.EmailField(blank=False)
    date = models.DateField()
    quantity = models.CharField(max_length=999, blank=False, validators=[RegexValidator(r'^[0-9+]', 'Solo números enteros')])