from django.db import models

# Create your models here.


class User(models.Model):
    date = models.DateField( auto_now=False, auto_now_add=False) 
    latitude_south = models.IntegerField( )
    
    
    
    # lat_axistilt = models.DecimalField( decimal_places=2)
    # lat_degree = models.IntegerField()
    # lat_minute = models.IntegerField()
    # lat_second = models.IntegerField()
    
    
    
    