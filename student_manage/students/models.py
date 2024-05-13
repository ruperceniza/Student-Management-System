from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    course = models.CharField(max_length=50, choices=[
        ('BS-CS', 'BS-CS'),
        ('BS-DS', 'BS-DS'),
        ('BS-IT', 'BS-IT'),
        ('BS-IS', 'BS-IS')
    ])
    gender = models.CharField(max_length=6, choices=[
        ('Male', 'Male'),
        ('Female', 'Female')
    ])
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
