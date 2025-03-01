from django.db import models

# Create your models here.
class Product(models.Model):
    date = models.DateField(auto_now_add=True) 
    destignation = models.CharField(max_length=255)
    referance = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=255)
    destination  = models.CharField(max_length=255)
    
    def __str__(self):
        return self.destignation
