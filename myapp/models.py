from django.db import models
from datetime import timedelta
from django.utils import timezone
from multiselectfield import MultiSelectField

class Student(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True)
    board = models.CharField(max_length=50, choices=[('CBSE', 'CBSE'), ('WBBSE', 'WBBSE'), ('ICSE', 'ICSE')])
    student_class = models.IntegerField(choices=[(1,1),(2,2),(3,3),(4,4),(5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)])
    # payment = models.CharField(max_length=50, choices=[('DONE', 'DONE'), ('NOT DONE', 'NOT DONE')], default='NOT DONE')
    subject = models.CharField(max_length=100, default='All')

    def __str__(self):
        return self.name

class Payment(models.Model):
    MONTH_CHOICES = [
        (1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'),
        (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'),
        (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=timezone.now)
    year = models.IntegerField()
    months = MultiSelectField(choices=MONTH_CHOICES, default=[1])

    def __str__(self):
        return f"{self.student.name} - {self.amount} - {self.year} - {self.months}"
    

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    subject_teaches = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Batch(models.Model):
    DAYS = [
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
        ('SUN', 'Sunday'),
    ]
    subject_name = models.CharField(max_length=100)
    batch_name = models.CharField(max_length=100,default="")
    batch_time = models.TimeField()
    batch_day = MultiSelectField(choices=DAYS)
    class_level = models.IntegerField(choices=[(1,1),(2,2),(3,3),(4,4),(5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)])
    class_mode = models.CharField(max_length=100, choices=[('ONLINE', 'ONLINE'), ('OFFLINE', 'OFFLINE')], default='ONLINE')  
    start_date = models.DateField(default=timezone.now) 
    teachers = models.ManyToManyField(Teacher, related_name='teachers')
    students = models.ManyToManyField(Student, related_name='students', blank=True)

    def __str__(self):
        return f"{self.subject_name} - {self.batch_day} at {self.batch_time}"


