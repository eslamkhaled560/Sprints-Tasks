from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    grade = models.CharField(max_length=10)


class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    credits = models.IntegerField()
