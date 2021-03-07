from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator

# Create your models here.

class Course(models.Model):
    course_code = models.CharField(primary_key=True, max_length=8, validators=[RegexValidator(regex='^[A-Z]{4}\d{4}$', \
        message='Course code needs to have 4 capital letters followed by 4 numbers')])
    course_name = models.CharField(max_length=30)

    def __str__(self):
        return self.course_code

class Student(models.Model):
    z_id = models.CharField(primary_key=True, max_length=8, validators=[RegexValidator(regex='^z\d{7}$', \
        message='zId needs to start with z followed by 7 numbers')])
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    courses = models.ManyToManyField(Course, through='Enrolment', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Enrolment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, to_field='z_id')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, to_field='course_code')
    term_taken = models.CharField(max_length=20)
    letter_grade = models.CharField(max_length=2, validators=[RegexValidator(regex='^(FL|PS|CR|DN|HD)$', \
        message='Grade needs to be one of FL, PS, CR, DN, HD')], null=True, blank=True)
    mark = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)

    def __str__(self):
        return f"{self.student}'s enrolment in {self.course}"