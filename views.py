from django.shortcuts import render, redirect
from crudApp.models import Student
from crudApp.forms import StudentForm

def read(request):
    student = Student.objects.all()
    return render(request, 'crudApp/index.html', {'student': student})

def create(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/read')  
    
    return render(request, 'crudApp/create.html', {'form': form})

def delete(request,id):
    student = Student.objects.get(id =id)
    student.delete()
    return redirect('/read')

def update(request,id):
    
    student = Student.objects.get(id=id)
    if request.method  == 'POST':
        form = StudentForm(request.POST,instance = student)
        if form.is_valid():
            form.save()
            return redirect('/read')
    return render(request, 'crudApp/update.html', {'student': student})