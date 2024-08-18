from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Batch
from .forms import StudentForm, BatchForm
from django.contrib import messages
from django.views.generic import DetailView
from django.db.models import Q

def index(request):
    search_query = request.GET.get("search", "")
    students = Student.objects.all()

    if search_query:
        students = students.filter(
            Q(name__icontains=search_query) |
            Q(phone_number__icontains=search_query) |
            Q(board__icontains=search_query) |
            Q(student_class__icontains=search_query) |
            Q(payment__icontains=search_query)
        )

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
        'search': search_query,
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
    search_query = request.GET.get('search', '')

    if search_query:
        batches = Batch.objects.filter(
            Q(subject_name__icontains=search_query) |
            Q(class_level__icontains=search_query) |
            Q(batch_day__icontains=search_query) |
            Q(teacher_name__icontains=search_query)
        )
    else:
        batches = Batch.objects.all()

    return render(request, 'view_batches.html', {'batches': batches})

class BatchDetailView(DetailView):
    model = Batch
    template_name = 'batch_detail.html'
    context_object_name = 'batch'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Exclude students already in the batch
        context['students'] = Student.objects.exclude(id__in=self.object.students.all())
        return context

def add_existing_students(request, pk):
    batch = get_object_or_404(Batch, pk=pk)
    if request.method == 'POST':
        student_ids = request.POST.getlist('existing_students')
        existing_students = batch.students.all().values_list('id', flat=True)
        new_students = [Student.objects.get(id=id) for id in student_ids if int(id) not in existing_students]
        duplicate_students = [Student.objects.get(id=id) for id in student_ids if int(id) in existing_students]
        
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

def edit_batch(request, id):
    batch = get_object_or_404(Batch, id=id)
    if request.method == "POST":
        form = BatchForm(request.POST, instance=batch)
        if form.is_valid():
            form.save()
            messages.success(request, 'Batch updated successfully!')
            return redirect('view_batches')
    else:
        form = BatchForm(instance=batch)
    return render(request, 'edit_batch.html', {'form': form})

def delete_batch(request, id):
    batch = get_object_or_404(Batch, id=id)
    if request.method == "POST":
        batch.delete()
        return redirect('view_batches')
    return render(request, 'confirm_delete.html', {'batch': batch})

def remove_student_from_batch(request, batch_id, student_id):
    batch = get_object_or_404(Batch, id=batch_id)
    student = get_object_or_404(Student, id=student_id)
    batch.students.remove(student)
    messages.success(request, f'{student.name} has been removed from the batch.')
    return redirect('batch_detail', pk=batch.id)