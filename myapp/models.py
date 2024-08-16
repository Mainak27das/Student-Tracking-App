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

class Batch(models.Model):
    subject_name = models.CharField(max_length=100)
    batch_time = models.TimeField()
    batch_day = models.CharField(max_length=20, choices=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday')
    ])
    batch_duration = models.DurationField(default="")  # Default 1-hour duration
    class_level = models.CharField(max_length=50, default="N/A")

    class_mode = models.CharField(max_length=100, default='Offline')  # Default as 'N/A'
    start_date = models.DateField(default=timezone.now)  # Default to current date
    teacher_name = models.CharField(max_length=100,default='N/A')
    students = models.ManyToManyField(Student, related_name='batches')

    def __str__(self):
        return f"{self.subject_name} - {self.batch_day} at {self.batch_time}"
