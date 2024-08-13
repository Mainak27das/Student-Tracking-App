# models.py
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    school = models.CharField(max_length=150)
    board = models.CharField(max_length=50, choices=[('CBSE', 'CBSE'), ('WBBSE', 'WBBSE'), ('ICSE', 'ICSE')])
    student_class = models.CharField(max_length=10)

    def __str__(self):
        return self.name
