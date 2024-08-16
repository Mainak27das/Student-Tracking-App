from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, default='N/A')  # Adding a default value
    board = models.CharField(max_length=50, choices=[('CBSE', 'CBSE'), ('WBBSE', 'WBBSE'), ('ICSE', 'ICSE')])
    student_class = models.CharField(max_length=10)
    payment = models.CharField(max_length=50, choices=[('DONE', 'DONE'), ('NOT DONE', 'NOT DONE')], default='NOT DONE')
    subject = models.CharField(max_length=100, default='All')  # Adding a subject field with a default value

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
    students = models.ManyToManyField(Student, related_name='batches')

    def __str__(self):
        return f"{self.subject_name} - {self.batch_day} at {self.batch_time}"
