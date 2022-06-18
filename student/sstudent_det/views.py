from multiprocessing import context
from django.shortcuts import render
from .forms import StudentForm
from .models import Student
from django.db.models import Q
# Create your views here.

def studentreg(request):
    form=StudentForm()
    context={'form':form}
    if request.method=='POST':
        if form.is_valid():
            
            branch=form.cleaned_data['branch']
            name=form.cleaned_data['branch']
            phone_number=form.cleaned_data['phone_number']
            email=form.cleaned_data['email']
            address=form.cleaned_data['address']
            photo=form.cleaned_data['photo']
            
            student=Student.objects.create(branch=branch,name=name,phone_number=phone_number,email=email,address=address,photo=photo)
            student.save()

    return render(request,'student.html',context)

def details(request):
    student=Student.objects.all()
    context={
        'student':student
    }
    return render(request,'student.html',context)

def update(request,pk):
    student=Student.objects.get(id=pk)
    if request.method=='POST':
        branch=request.POST['branch']
        name=request.POST['branch']
        phone_number=request.POST['phone_number']
        email=request.POST['email']
        address=request.POST['address']
        photo=request.POST['photo']

        student.branch=branch
        student.name=name
        student.phone_number=phone_number
        student.email=email
        student.save()
    return render(request,'update.html')

def delete(request,pk):
    student=Student.objects.get(id=pk)
    student.delete()

def search(request):
    if request.method=='POST':
        query=request.POST['query']
        student=Student.objects.filter(Q(id=query)|Q(phone_number=query)|Q(email=query))
        context={'student':student}
        return render(request,'search.html',context)