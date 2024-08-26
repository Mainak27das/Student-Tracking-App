from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Batch,Teacher, Payment
from .forms import StudentForm, BatchForm,TeacherForm
from django.contrib import messages
from django.views.generic import DetailView
from django.db.models import Q
from django.utils.dateparse import parse_date
from django.db import models

# Home Page with Student List and Search
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
        'batch_form': BatchForm(),
    }
    return render(request, 'index.html', context)

# Student Profile Page
def student_profile(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    batches = Batch.objects.filter(students=student)
    payments = Payment.objects.filter(student=student)
    context = {
        'student': student,
        'batches': batches,
        'payments': payments,
    }
    return render(request, 'student_profile.html', context)

# Create a New Batch
def create_batch(request):
    if request.method == "POST":
        form = BatchForm(request.POST)
        print(request.method)
        if form.is_valid():
            form.save()
            messages.success(request, "Batch created successfully!")
            return redirect('view_batches')
        else:
            print(form.errors)
            messages.error(request, "Error creating batch. Please try again.")
    else:
        form = BatchForm()
    return redirect('index')
    # return render(request, 'wrong.html', {'form': form})

# View All Batches
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

# Batch Detail View
class BatchDetailView(DetailView):
    model = Batch
    template_name = 'batch_detail.html'
    context_object_name = 'batch'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET.get('search_batch_student'):
            search_query = self.request.GET.get('search_batch_student')
            students = Student.objects.filter(
                Q(name__icontains=search_query) |
                Q(phone_number__icontains=search_query) |
                Q(board__icontains=search_query) |
                Q(student_class__icontains=search_query) |
                Q(payment__icontains=search_query)
            )
            context['students'] = students.filter(batches=self.object)
            
        else:
            context['students'] = self.object.students.all()
        
        if self.request.GET.get('search_remaining_student'):
            search_query = self.request.GET.get('search_remaining_student')
            context['remaining_students'] = Student.objects.exclude(id__in=self.object.students.all()).filter(
                Q(name__icontains=search_query) |
                Q(phone_number__icontains=search_query) |
                Q(board__icontains=search_query) |
                Q(student_class__icontains=search_query) |
                Q(payment__icontains=search_query)
            )
        else:
            context['remaining_students'] = Student.objects.exclude(id__in=self.object.students.all())
        context['student_form'] = StudentForm()
        return context

# Add Existing Students to a Batch
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

# Add a New Student to a Batch
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
            # print(form.errors)
            messages.error(request, "Error adding student. Please try again.")
            return redirect('batch_detail', pk=pk)

    else:
        form = StudentForm()
    return redirect('batch_detail', pk=pk)
    # return render(request, 'add_new_student.html', {'form': form})

# Edit Batch Details
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

# Delete a Batch
def delete_batch(request, id):
    batch = get_object_or_404(Batch, id=id)
    if request.method == "POST":
        batch.delete()
        messages.success(request, 'Batch deleted successfully!')
        return redirect('view_batches')
    return render(request, 'confirm_delete.html', {'batch': batch})

# Remove a Student from a Batch
def remove_student_from_batch(request, batch_id, student_id):
    batch = get_object_or_404(Batch, id=batch_id)
    student = get_object_or_404(Student, id=student_id)
    batch.students.remove(student)
    messages.success(request, f'{student.name} has been removed from the batch.')
    return redirect('batch_detail', pk=batch.id)

# Edit Student Profile
def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student profile updated successfully!')
            return redirect('student_profile', student_id=student.id)
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit_student.html', {'form': form, 'student': student})

# Delete Student Profile
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student profile deleted successfully!')
        return redirect('index')
    return render(request, 'confirm_delete_student.html', {'student': student})

# Add a Teacher/Instructor
def add_teacher(request):
    search_query = request.GET.get('search', '')  # Get the search query

    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Teacher added successfully!')
            return redirect('add_teacher')  # Redirect to the same page after saving
    else:
        form = TeacherForm()

    # Filter teachers based on search query
    if search_query:
        teachers = Teacher.objects.filter(
            Q(name__icontains=search_query) |
            Q(phone_number__icontains=search_query) |
            Q(subject_teaches__icontains=search_query) |
            Q(qualification__icontains=search_query)
        )
    else:
        teachers = Teacher.objects.all()

    return render(request, 'add_teacher.html', {'form': form, 'teachers': teachers, 'search': search_query})


# Edit teacher view
def edit_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            messages.success(request, 'Teacher table updated successfully!')
            return redirect('add_teacher')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'edit_teacher.html', {'form': form})

# Delete teacher view
def delete_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    if request.method == 'POST':
        teacher.delete()
        messages.success(request, 'Teacher table Deleted successfully!')
        return redirect('add_teacher')



def payment_record(request, student_id):
    if request.method == "POST":
        
        student = get_object_or_404(Student, id=student_id)
        amount = request.POST['payment']
        payment_method = request.POST.get('payment_method')
        payment_date = request.POST.get('payment_date')
        payment_month = request.POST.getlist('payment_months')
        payment_year = request.POST.get('payment_year')

        payment = Payment.objects.create(
            student=student,
            amount=amount,
            payment_method=payment_method,
            date=payment_date,
            year=payment_year,
            months=payment_month
        )
        payment.save()

        messages.success(request, 'Payment recorded successfully!')
    return redirect("student_profile", student_id=student_id)

def all_payment(request):
    context = {}
    payments = Payment.objects.all().order_by('-date')

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    if start_date and end_date:
        start_date = parse_date(start_date)
        end_date = parse_date(end_date)
        payments = payments.filter(date__range=[start_date, end_date])
        total_amount = payments.aggregate(total_amount=models.Sum('amount'))['total_amount']
        context['total_amount'] = total_amount
    
    context['payments'] = payments
    return render(request, 'all_payments.html', context)