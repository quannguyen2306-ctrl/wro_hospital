from tkinter import CASCADE
from django.db import models
# from django.contrib.postgres.fields import ArrayField

# Create your models here.
class medicine(models.Model):
    name = models.CharField(max_length=200)
    # amount = models.CharField(max_length=120)

    def __str__(self):
        return self.name

# class Patient(models.Model):
#     patientID = models.ForeignKey(pillList, on_delete=models.CASCADE)
#     medicineList = models.JSONField

# class Example(models.Model):
#     data = models.JSONField()

class PatientMedicine(models.Model):
    data = models.JSONField()




    

            



