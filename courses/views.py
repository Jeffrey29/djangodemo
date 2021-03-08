from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Student, Enrolment
from .serializers import CourseSerializer, StudentSerializer, EnrolmentSerializer
from .forms import NewStudentForm, EditStudentForm
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
    form_class = NewStudentForm
    success_url = reverse_lazy('courses:all_students')

class EditStudent(generic.UpdateView):
    model = Student 
    form_class = EditStudentForm
    template_name = 'courses/edit_student.html'
    
    def get_success_url(self, **kwargs):         
        return reverse_lazy('courses:student_detail', args=(self.object.z_id,))

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        student.delete()
        print('delete here')
        return redirect('courses:all_students')

    return redirect('courses:all_students')