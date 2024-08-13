from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.contrib import messages

def index(request):
    students = Student.objects.all()
    total_students = students.count()
    cbse_students = students.filter(board='CBSE').count()
    wbbse_students = students.filter(board='WBBSE').count()
    icse_students = students.filter(board='ICSE').count()

    context = {
        'students': students,
        'total_students': total_students,
        'cbse_students': cbse_students,
        'wbbse_students': wbbse_students,
        'icse_students': icse_students,
    }
    return render(request, 'index.html', context)

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " Student Added !! ")
            return redirect('index')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})


def search(request):
    search = request.GET.get("search", "")
    
    if len(search) > 80:
        all_students = Student.objects.none()
    else:
        # Filter based on available fields in the Student model
        all_students_name = Student.objects.filter(name__icontains=search)
        all_students_school = Student.objects.filter(school__icontains=search)
        all_students_board = Student.objects.filter(board__icontains=search)
        all_students_class = Student.objects.filter(student_class__icontains=search)
        
        # Combine all querysets
        all_students = all_students_name.union(all_students_school, all_students_board, all_students_class)
    
    context = {"students": all_students, "search": search}
    return render(request, "search.html", context)


def student_profile(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    context = {'student': student}
    return render(request, 'student_profile.html', context)