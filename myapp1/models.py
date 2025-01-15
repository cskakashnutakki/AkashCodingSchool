from django.db import models

# Create your models here.
class callback(models.Model):
    name=models.CharField(max_length=25)
    phone=models.IntegerField()
    datetime=models.DateTimeField()

class courses(models.Model):
    name=models.CharField(max_length=25)
    lang=models.CharField(max_length=10)
    price=models.IntegerField()
    image=models.ImageField(upload_to='images/')
