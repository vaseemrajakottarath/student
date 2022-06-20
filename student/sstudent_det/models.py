from distutils.command.upload import upload
from email.headerregistry import Address
from django.db import models
from django.db.models import Max

# Create your models here.

class Student(models.Model):
    # id=models.CharField(primary_key=True,editable=False,max_length=5)
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

    # def save(self, **kwargs):
    #     if not self.id:
    #         max = Student.objects.aggregate(id_max=Max('id'))['id_max']
    #         self.id = "{}".format('STU_', max if max is not None else 1)
    #     super().save(*kwargs)