from django.db import models


class volenteer(models.Model):
    name=models.CharField(max_length=50)
    email = models.EmailField()
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.name


class raindata(models.Model):
    enterytime=models.DateTimeField()
    rain=models.IntegerField()

    def __str__(self):
        return "%s - %s " % (self.id, self.rain)








