from pyexpat import model
from django.forms import ModelForm
from .models import Student

class StudentForm(ModelForm):
    class Meta:
        model=Student
        fields=['branch','name','phone_number','email','Address','photo']

class MarkForm(ModelForm):
    class Meta:
        model=Student
        fields=['SUB1','SUB2','SUB3']

    # BRANCH_CHOICES=(
    # ('CS','CS'),
    # ('EC','EC'),
    # ('MECH','MECH'))
    # branch=forms.ChoiceField(choices=BRANCH_CHOICES,widget=forms.Select(attrs={
    #     'class':'form-control col-12 mb-3',
    #     'placeholder':'BRANCH',
    # }),label='')
    # name=forms.CharField(widget=forms.TextInput(attrs={
    #     'class':'form-control col-12 mb-3',
    #     'row':'3',
    #     'placeholder':'name',
    # }))
    # phone_number=forms.IntegerField()
    # email=forms.EmailField()
    # address=forms.CharField()
    # image=forms.ImageField()