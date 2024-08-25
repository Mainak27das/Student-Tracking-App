from django import forms
from .models import Student,Batch,Teacher

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
        # fields = [
        #     'subject_name', 'batch_name', 'batch_time', 'batch_day',
        #     'class_level', 'class_mode', 'start_date', 'teachers'
        # ]
        fields = ['subject_name', 'batch_name', 'batch_time', 'batch_day', 'start_date', 'class_level', 'class_mode', 'teachers']
        widgets = {
            'subject_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter subject name'}),
            'batch_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter batch name'}),
            'batch_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'batch_day': forms.CheckboxSelectMultiple(),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'class_level': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Enter class level'}),
            'class_mode': forms.Select(attrs={'class': 'form-control'}),
            'teachers': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'phone_number', 'subject_teaches', 'qualification']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter teacher name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'subject_teaches': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter subject taught'}),
            'qualification': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter qualification'}),
        }