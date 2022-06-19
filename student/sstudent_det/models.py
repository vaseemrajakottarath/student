from distutils.command.upload import upload
from email.headerregistry import Address
from django.db import models

# Create your models here.

class Student(models.Model):
    BRANCH_CHOICES=(
    ('CS','CS'),
    ('EC','EC'),
    ('MECH','MECH'))
    branch=models.CharField(max_length=50,choices=BRANCH_CHOICES)
    name=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=10,unique=True)
    email=models.EmailField(unique=True)
    Address=models.TextField()
    photo=models.ImageField(upload_to='images/')
    
    SUB1=models.CharField(max_length=10,null=True,blank=True)
    SUB2=models.CharField(max_length=10,null=True,blank=True)
    SUB3=models.CharField(max_length=10,null=True,blank=True)

    def __str__(self):
        return self.name