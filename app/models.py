from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class User(models.Model):
    date = models.DateTimeField()
    latitude_south = models.PositiveIntegerField()
    
    

    
    
    
    