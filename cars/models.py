from django.db import models

# Create your models here.
class Car(models.Model):  
    cid = models.CharField(primary_key=True,max_length=20) 
    cname = models.CharField(max_length=30)  
    ccolor = models.CharField(max_length=20)  
    class Meta:  
        db_table = "Car"  