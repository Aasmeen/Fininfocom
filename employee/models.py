from django.db import models
from django.contrib.postgres.fields import ArrayField
from drf_extra_fields.fields import Base64ImageField


class Employee(models.Model):
    name = models.CharField()
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    gender = models.CharField()
    phoneNo = models.CharField()
    addressDetails = models.JSONField()
    workExperience = ArrayField(models.JSONField())
    qualifications = ArrayField(models.JSONField())
    projects = ArrayField(models.JSONField())
    photo = Base64ImageField()
