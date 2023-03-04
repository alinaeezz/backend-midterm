from django.db import models

class Employees(models.Model):
    full_name = models.CharField(max_length=255, null=False)
    position = models.CharField(null=False)
    salary = models.IntegerField(max_length=255, unique=True, null=False)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

