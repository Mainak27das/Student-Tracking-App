from django import forms
from .models import Student,Batch

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'phone_number', 'board', 'student_class', 'payment', 'subject']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter student name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'board': forms.Select(attrs={'class': 'form-control'}),  # 'board' is a choice field
            'student_class': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter class'}),
            'payment': forms.Select(attrs={'class': 'form-control'}),  # 'payment' is a choice field
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter subject'}),
        }

class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = [
            'subject_name', 'batch_time', 'batch_day', 'batch_duration', 
            'class_level', 'class_mode', 'start_date', 'teacher_name'
        ]
        widgets = {
            'batch_time': forms.TimeInput(attrs={'type': 'time'}),
            'batch_day': forms.Select(choices=[
                ('Monday', 'Monday'),
                ('Tuesday', 'Tuesday'),
                ('Wednesday', 'Wednesday'),
                ('Thursday', 'Thursday'),
                ('Friday', 'Friday'),
                ('Saturday', 'Saturday'),
                ('Sunday', 'Sunday')
            ]),
            'batch_duration': forms.TimeInput(attrs={'type': 'time'}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'batch_status': forms.Select(choices=[
                ('Active', 'Active'),
                ('Inactive', 'Inactive')
            ]),
        }
