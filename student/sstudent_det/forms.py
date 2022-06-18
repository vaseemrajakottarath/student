from django import forms

class StudentForm(forms.Form):
    BRANCH_CHOICES=(
    ('CS','CS'),
    ('EC','EC'),
    ('MECH','MECH'))
    branch=forms.ChoiceField(choices=BRANCH_CHOICES,widget=forms.Select(attrs={
        'class':'form-control col-12 mb-3',
        'placeholder':'BRANCH',
    }),label='')
    name=forms.CharField(max_length=50)
    phone_number=forms.IntegerField()
    email=forms.EmailField()
    address=forms.Textarea()
    image=forms.ImageField()