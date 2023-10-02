from django.db import models

class Employee(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    Phone = models.IntegerField(null=True)
    Joined = models.DateField(null=True)
    Departement = models.CharField(max_length=200) 
    
    