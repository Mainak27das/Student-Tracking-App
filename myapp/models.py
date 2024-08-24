from django.db import models
from datetime import timedelta
from django.utils import timezone

class Student(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, default='N/A')
    board = models.CharField(max_length=50, choices=[('CBSE', 'CBSE'), ('WBBSE', 'WBBSE'), ('ICSE', 'ICSE')])
    student_class = models.CharField(max_length=10)
    payment = models.CharField(max_length=50, choices=[('DONE', 'DONE'), ('NOT DONE', 'NOT DONE')], default='NOT DONE')
    subject = models.CharField(max_length=100, default='All')

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    subject_teaches = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Batch(models.Model):
    days = [
        ('MON', 'MONDAY'),
        ('TUE', 'TUESDAY'),
        ('WED', 'WEDNESDAY'),
        ('THU', 'THURSDAY'),
        ('FRI', 'FRIDAY'),
        ('SAT', 'SATURDAY'),
        ('SUN', 'SUNDAY'),
    ]
    subject_name = models.CharField(max_length=100)
    batch_name = models.CharField(max_length=100,default="")
    batch_time = models.TimeField()
    batch_day = models.CharField(max_length=50, choices=days)
    class_level = models.IntegerField(choices=[(1,1),(2,2),(3,3),(4,4),(5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)])

    class_mode = models.CharField(max_length=100, choices=[('ONLINE', 'ONLINE'), ('OFFLINE', 'OFFLINE')], default='ONLINE')  
    start_date = models.DateField(default=timezone.now) 
    teachers = models.ManyToManyField(Teacher, related_name='teachers')
    students = models.ManyToManyField(Student, related_name='students', blank=True, null=True)

    def __str__(self):
        return f"{self.subject_name} - {self.batch_day} at {self.batch_time}"


