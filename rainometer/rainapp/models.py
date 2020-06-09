from django.db import models

class Volenteer(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
class Rainstation(models.Model):
    id = models.AutoField(primary_key=True)
    location= models.CharField(max_length=30)

class Rain(models.Model):
    entry = models.ForeignKey(Rainstation, on_delete=models.CASCADE)



