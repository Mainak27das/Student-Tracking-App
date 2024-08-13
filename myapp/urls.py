from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
   path('',views.index,name='index'),
   path('add/', views.add_student, name='add_student'),
   # path('edit/<int:student_id>/', views.edit_student, name='edit_student'),
   path("search", views.search, name="search"),
]