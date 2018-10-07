from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(name="Name", max_length=255)
    surname = models.CharField(name="Surname", max_length=255)