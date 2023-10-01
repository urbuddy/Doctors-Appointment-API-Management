from django.db import models


# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    max_patients = models.IntegerField()
    # Other doctor details like specialization, etc.


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    patient_name = models.CharField(max_length=100)
    # Other appointment details
