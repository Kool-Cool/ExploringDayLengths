from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class User(models.Model):
    date = models.DateField(
                            default=1,
                            validators=[
                                MinValueValidator(0),
                                MaxValueValidator(5)]
                            ) 
    latitude_south = models.PositiveIntegerField()
    
    

    
    
    
    