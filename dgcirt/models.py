from django.db import models

# Create your models here.
class Person(models.Model):
    firstName=models.CharField(max_length=20)
    secondName=models.CharField(max_length=20)
    course=models.CharField(max_length=60)
    courseDetails=models.TextField(max_length=100)
    companyLink = models.URLField(max_length=80)
    companyName=models.CharField(max_length=30)
    ceoName=models.CharField(max_length=30)
