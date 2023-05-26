from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator # NEW
from django.core import validators

# Create your models here.


class User(models.Model):
    date = models.PositiveIntegerField(("Day"),default=1,
                                       validators=[
                                           MaxValueValidator(31),
                                           MinValueValidator(1),
                                            ]
                                       )
    month = models.PositiveIntegerField(default=1,
                                       validators=[
                                           MaxValueValidator(12),
                                           MinValueValidator(1),
                                            ]
                                       )
    
    year = models.PositiveIntegerField(default=2023)
    
    latitude = models.DecimalField(("Latitude (In degrees)"), decimal_places=2 , max_digits=2,default=51.50)
    
    

    
    
    
    