from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

# def index(request):
#     return render(request,'index.html')

def index(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

# def edit_student(request, student_id):
#     student = get_object_or_404(Student, id=student_id)
#     if request.method == 'POST':
#         form = StudentForm(request.POST, instance=student)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = StudentForm(instance=student)
#     return render(request, 'edit_student.html', {'form': form, 'student': student})