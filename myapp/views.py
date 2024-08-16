from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Batch
from .forms import StudentForm, BatchForm
from django.contrib import messages
from django.views.generic import DetailView

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
            messages.success(request, "Student Added!!")
            return redirect('index')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

def search(request):
    search = request.GET.get("search", "")
    
    if len(search) > 80:
        all_students = Student.objects.none()
    else:
        all_students_name = Student.objects.filter(name__icontains=search)
        all_students_phone = Student.objects.filter(phone_number__icontains=search)
        all_students_board = Student.objects.filter(board__icontains=search)
        all_students_class = Student.objects.filter(student_class__icontains=search)
        all_students_payment = Student.objects.filter(payment__icontains=search)
        
        all_students = all_students_name.union(
            all_students_phone, 
            all_students_board, 
            all_students_class, 
            all_students_payment
        )
    
    context = {"students": all_students, "search": search}
    return render(request, "search.html", context)

def student_profile(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    context = {
        'student': student,
    }
    return render(request, 'student_profile.html', context)

def create_batch(request):
    if request.method == "POST":
        form = BatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BatchForm()
    return render(request, 'create_batch.html', {'form': form})

def view_batches(request):
    batches = Batch.objects.all()
    return render(request, 'view_batches.html', {'batches': batches})

class BatchDetailView(DetailView):
    model = Batch
    template_name = 'batch_detail.html'
    context_object_name = 'batch'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = Student.objects.all()
        return context

def add_existing_students(request, pk):
    batch = get_object_or_404(Batch, pk=pk)
    if request.method == 'POST':
        student_ids = request.POST.getlist('existing_students')
        existing_students = batch.students.all().values_list('id', flat=True)
        new_students = [Student.objects.get(id=id) for id in student_ids if id not in existing_students]
        duplicate_students = [Student.objects.get(id=id) for id in student_ids if id in existing_students]
        
        if new_students:
            batch.students.add(*new_students)
            messages.success(request, "Students successfully added to the batch.")
        if duplicate_students:
            messages.info(request, "Some students are already in this batch.")
    
    return redirect('batch_detail', pk=pk)

def add_new_student(request, pk):
    batch = get_object_or_404(Batch, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student = form.save()
            batch.students.add(new_student)
            messages.success(request, "New student added to the batch.")
            return redirect('batch_detail', pk=pk)
    else:
        form = StudentForm()
    return render(request, 'add_new_student.html', {'form': form})
