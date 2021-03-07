from django.shortcuts import render
from .models import Course, Student, Enrolment
from .serializers import CourseSerializer, StudentSerializer, EnrolmentSerializer
from .forms import NewStudentForm
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, renderers, generics
from rest_framework.decorators import action
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.
    
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('z_id')
    serializer_class = StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by('course_code')
    serializer_class = CourseSerializer

class EnrolmentViewSet(viewsets.ModelViewSet):
    queryset = Enrolment.objects.all().order_by('student')
    serializer_class = EnrolmentSerializer

class AllStudentsView(generic.ListView):
    model = Student 
    queryset = Student.objects.all()
    context_object_name = 'all_students'
    template_name = 'courses/all_students.html'

class StudentDetailView(generic.DetailView):
    model = Student 
    template_name = 'courses/student_detail.html'

class NewStudent(generic.CreateView):
    model = Student 
    template_name = 'courses/new_student.html'
    # fields = ('z_id', 'first_name', 'last_name', 'courses')
    form_class = NewStudentForm
    success_url = reverse_lazy('courses:all_students')