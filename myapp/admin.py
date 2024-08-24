from django.contrib import admin
from myapp.models import Student,Batch,Teacher
from myapp.forms import BatchForm


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	list_display = ['name', 'phone_number', 'board', 'student_class', 'payment', 'subject']
	search_fields = ['name', 'phone_number', 'board', 'student_class', 'payment', 'subject']
	list_filter = ['board', 'student_class', 'payment', 'subject']
	list_per_page = 10

@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
	list_display = ['subject_name', 'batch_name', 'batch_time', 'batch_day', 'class_level', 'class_mode', 'start_date']
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