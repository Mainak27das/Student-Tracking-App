from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'school', 'board', 'student_class']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter student name'}),
            'school': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter school name'}),
            'board': forms.Select(attrs={'class': 'form-control'}),  # Assuming 'board' is a choice field in the model
            'student_class': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter class'}),
        }
