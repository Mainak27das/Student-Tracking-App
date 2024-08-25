from django.contrib import admin
from django.urls import path
from myapp import views
from .views import create_batch, view_batches, BatchDetailView, add_existing_students, add_new_student,edit_teacher, delete_teacher

urlpatterns = [
    path('', views.index, name='index'),
    # path('edit/<int:student_id>/', views.edit_student, name='edit_student'),  # Uncomment if needed
    path('student/<int:student_id>/', views.student_profile, name='student_profile'),
    path('create-batch/', create_batch, name='create_batch'),
    path('view-batches/', view_batches, name='view_batches'),
    path('batch/<int:pk>/', BatchDetailView.as_view(), name='batch_detail'),
    path('batch/<int:pk>/add-existing-students/', add_existing_students, name='add_existing_students'),
    path('batch/<int:pk>/add-new-student/', add_new_student, name='add_new_student'),
    path('edit-batch/<int:id>/', views.edit_batch, name='edit_batch'),
    # Ensure there's also a delete_batch path
    path('delete-batch/<int:id>/', views.delete_batch, name='delete_batch'),
    path('batch/<int:batch_id>/remove_student/<int:student_id>/', views.remove_student_from_batch, name='remove_student_from_batch'),

    path('student/<int:student_id>/edit/', views.edit_student, name='edit_student'),
    path('student/<int:student_id>/delete/', views.delete_student, name='delete_student'),

    path('add-teacher/', views.add_teacher, name='add_teacher'),

    path('edit_teacher/<int:teacher_id>/', edit_teacher, name='edit_teacher'),
    path('delete_teacher/<int:teacher_id>/', delete_teacher, name='delete_teacher'),
	

    path('add-payment/<int:student_id>', views.payment_record, name='payment_record'),
]


