from rest_framework import serializers
from .models import Course, Student, Enrolment

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_code', 'course_name']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['z_id', 'first_name', 'last_name', 'courses']

class EnrolmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrolment 
        fields = ['id', 'student', 'course', 'term_taken', 'letter_grade', 'mark']
