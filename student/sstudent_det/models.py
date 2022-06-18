from email.headerregistry import Address
from django.db import models

# Create your models here.

class Student(models.Model):
    BRANCH_CHOICES=(
    ('CS','CS'),
    ('EC','EC'),
    ('MECH','MECH'))
    branch=models.CharField(max_length=50,choice=BRANCH_CHOICES)
    name=models.CharField(max_length=50)
    phone_number=models.CharField(unique=True)
    email=models.EmailField(unique=True)
    Address=models.TextField()
    photo=models.ImageField()
