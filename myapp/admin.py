from django.contrib import admin
from myapp.models import Student,Batch,Teacher, Payment
from myapp.forms import BatchForm


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	list_display = ['name', 'phone_number', 'board', 'student_class', 'subject']
	search_fields = ['name', 'phone_number', 'board', 'student_class', 'subject']
	list_filter = ['board', 'student_class', 'subject']
	list_per_page = 10

@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
	list_display = ['id','subject_name', 'batch_name', 'batch_time', 'batch_day', 'class_level', 'class_mode', 'start_date']
	search_fields = ['subject_name', 'batch_name', 'batch_time', 'batch_day', 'class_level', 'class_mode', 'start_date']
	list_filter = ['subject_name', 'batch_name', 'batch_time', 'batch_day', 'class_level', 'class_mode', 'start_date']
	list_per_page = 10
	# form = BatchForm

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
	list_display = ['name', 'phone_number', 'subject_teaches', 'qualification']
	search_fields = ['name', 'phone_number', 'subject_teaches', 'qualification']
	list_filter = ['name', 'phone_number', 'subject_teaches', 'qualification']
	list_per_page = 10

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
	list_display = ['student', 'amount', 'date']
	search_fields = ['student', 'amount', 'date']
	list_filter = ['student', 'amount', 'date']
	list_per_page = 10