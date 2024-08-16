from django.contrib import admin
from django.urls import path
from myapp import views
from .views import create_batch, view_batches, BatchDetailView, add_existing_students, add_new_student

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_student, name='add_student'),
    # path('edit/<int:student_id>/', views.edit_student, name='edit_student'),  # Uncomment if needed
    path("search", views.search, name="search"),
    path('student/<int:student_id>/', views.student_profile, name='student_profile'),
    path('create-batch/', create_batch, name='create_batch'),
    path('view-batches/', view_batches, name='view_batches'),
    path('batch/<int:pk>/', BatchDetailView.as_view(), name='batch_detail'),
    path('batch/<int:pk>/add-existing-students/', add_existing_students, name='add_existing_students'),
    path('batch/<int:pk>/add-new-student/', add_new_student, name='add_new_student'),
]
