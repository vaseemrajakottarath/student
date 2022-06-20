from multiprocessing import context
from re import I
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import StudentForm,MarkForm
from .models import Student
from django.db.models import Q
# Create your views here.

def studentreg(request):
    
    if request.method=='POST':

        form=StudentForm(request.POST,request.FILES)
        if form.is_valid():
            branch=form.cleaned_data['branch']
            name=form.cleaned_data['name']
            phone_number=form.cleaned_data['phone_number']
            email=form.cleaned_data['email']
            address=form.cleaned_data['Address']
            photo=form.cleaned_data['photo']
                
            student=Student.objects.create(branch=branch,name=name,phone_number=phone_number,email=email,Address=address,photo=photo)
            student.save()
            return HttpResponse("Success")
    form=StudentForm()
    context={'form':form}
    return render(request,'student.html',context)

def details(request):
    student=Student.objects.all()
    context={
        'student':student
    }
    return render(request,'student.html',context)

def student_detail(request,pk):  
    student=Student.objects.filter(id=pk)
    print(student)
    context={'student':student}
    return render(request,'student_detail.html',context)


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
        query=request.POST['search']
        student=Student.objects.get(Q(phone_number=query)|Q(email=query)|Q(id__contains=query))
        print(student)
        ido=student.id
        print(ido)
        return redirect('student_detail',pk=ido)
    return render(request,'search.html')

def add_mark(request,pk):
    form=MarkForm()
    context={
        'form':form
    }
    if request.method=='POST':
        form=MarkForm(request.POST)
        if form.is_valid():
            sub1=form.cleaned_data['SUB1']
            sub2=form.cleaned_data['SUB2']
            sub3=form.cleaned_data['SUB3']

            student=Student.objects.get(id=pk)
            student.SUB1=sub1
            student.SUB2=sub2
            student.SUB3=sub3

            student.save()
            return redirect('student_detail',pk=pk)

    return render(request,'mark.html',context)