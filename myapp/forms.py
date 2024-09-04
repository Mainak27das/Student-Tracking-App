from django import forms
from .models import Student,Batch,Teacher, Payment, Parent
from datetime import datetime


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'phone_number', 'board', 'student_class', 'subject', 'addmission_date', 'fees']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter student name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'board': forms.Select(attrs={'class': 'form-control'}),  
            'student_class': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Enter class'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter subject'}),
            'addmission_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fees': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter fees'}),            
        }

class BatchForm(forms.ModelForm):
    MON = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type':'time'}), label='Monday', required=False)
    TUE = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type':'time'}), label='Tuesday', required=False)
    WED = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type':'time'}), label='Wednesday', required=False)
    THU = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type':'time'}), label='Thursday', required=False)
    FRI = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type':'time'}), label='Friday', required=False)
    SAT = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type':'time'}), label='Saturday', required=False)
    SUN = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type':'time'}), label='Sunday', required=False)
    class Meta:
        model = Batch
        fields = ['subject_name', 'batch_name', 'batch_day', 'start_date', 'class_level', 'class_mode', 'teachers']
        widgets = {
            'subject_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter subject name'}),
            'batch_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter batch name'}),
            'batch_day': forms.CheckboxSelectMultiple(),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'class_level': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Enter class level'}),
            'class_mode': forms.Select(attrs={'class': 'form-control'}),
            'teachers': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def clean(self):
        print("data cleaning\n\n")
        cleaned_data = super().clean()
        batch_times = {
            'MON': cleaned_data.get('MON'),
            'TUE': cleaned_data.get('TUE'),
            'WED': cleaned_data.get('WED'),
            'THU': cleaned_data.get('THU'),
            'FRI': cleaned_data.get('FRI'),
            'SAT': cleaned_data.get('SAT'),
            'SUN': cleaned_data.get('SUN'),
        }
        # Remove None values
        batch_times = {k: v.strftime('%I:%M:%p') for k, v in batch_times.items() if v is not None}
        cleaned_data['batch_times'] = batch_times
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.batch_times = self.cleaned_data.get('batch_times', {}) 
        if commit:
            instance.save()
            self.save_m2m()
        return instance


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

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'due_amount', 'payment_method', 'date', 'months']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter amount'}),
            'due_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter due amount'}),
            'payment_method': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'months': forms.CheckboxSelectMultiple(),
        }


class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ['father_name', 'mother_name', 'father_phone_number', 'mother_phone_number']
        widgets = {
            'father_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter father name'}),
            'mother_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter mother name'}),
            'father_phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter father phone number'}),
            'mother_phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter mother phone number'}),
            'child': forms.Select(attrs={'class': 'form-control'}),
        }