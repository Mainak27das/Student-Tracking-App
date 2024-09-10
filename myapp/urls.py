from django.contrib.auth import views as auth_views
from django.urls import path
from myapp import views
from .views import create_batch, view_batches, BatchDetailView, add_existing_students, add_new_student,edit_teacher, delete_teacher

urlpatterns = [
    path('', views.index, name='index'),
    # path('edit/<int:student_id>/', views.edit_student, name='edit_student'),  # Uncomment if needed
    path('student/<int:student_id>/', views.student_profile, name='student_profile'),
	path('filter-student/', views.filter_students, name='filter_student'),
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
	path('all-payments/', views.all_payment, name='all_payments'),
	
	path('update-payment/<int:id>/<int:std_id>/', views.edit_payment, name='update_payment'),

    path('add-parent/<int:std_id>/',views.add_parent, name="add_parent"),
    path('edit-parent/<int:id>/<int:std_id>/',views.edit_parent, name="edit_parent"),
	


    path('accounts/login/', views.user_login, name='login'),    
    path('accounts/logout/', views.user_logout, name='logout'),
	

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]


