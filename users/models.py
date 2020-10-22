from django.db import models

class User(models.Model):
    first_name  = models.CharField(max_length=45)
    last_name   = models.CharField(max_length=45)
    birth_date  = models.DateField()
    email       = models.EmailField(max_length=255, unique=True)
    password    = models.CharField(max_length=1000)
    
    class Meta:
        db_table = 'users'  
