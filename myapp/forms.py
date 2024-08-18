from django import forms
from .models import Student,Batch

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'phone_number', 'board', 'student_class', 'payment', 'subject']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter student name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'board': forms.Select(attrs={'class': 'form-control'}),  
            'student_class': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter class'}),
            'payment': forms.Select(attrs={'class': 'form-control'}), 
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter subject'}),
        }

class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = [
            'subject_name', 'batch_time', 'batch_day','batch_name',
            'class_level', 'class_mode', 'start_date', 'teacher_name'
        ]
        widgets = {
            'subject_name': forms.TextInput(attrs={'class': 'form-control'}),
            'batch_name': forms.TextInput(attrs={'class': 'form-control'}),
            'batch_time': forms.TimeInput(attrs={'type': 'time'}),
            'batch_day': forms.TextInput(attrs={'class': 'form-control'}), 
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'class_level': forms.TextInput(attrs={'class': 'form-control'}),
            'class_mode': forms.TextInput(attrs={'class': 'form-control'}),
            'teacher_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
