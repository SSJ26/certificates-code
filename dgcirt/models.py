from django.db import models

# Create your models here.
class Person(models.Model):
    firstName=models.CharField(max_length=20)
    secondName=models.CharField(max_length=20)
    course=models.CharField(max_length=60)
    courseDetails=models.TextField(max_length=80)
    companyLink = models.URLField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)
    companyName=models.CharField(max_length=50)
    ceoName=models.CharField(max_length=50)
