from django.contrib import admin
from .models import Doctor, Appointment

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Appointment)