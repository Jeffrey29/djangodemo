from django.urls import path, include
from . import views 
from django.views.generic import TemplateView
from rest_framework import routers

app_name = 'courses'

router = routers.DefaultRouter()
router.register('students', views.StudentViewSet)
router.register('courses', views.CourseViewSet)
router.register('enrolments', views.EnrolmentViewSet)

urlpatterns = [
    path('', TemplateView.as_view(template_name="courses/index.html"), name='students_home'),
    path('students/', views.AllStudentsView.as_view(), name='all_students'),
    path('new-student/', views.NewStudent.as_view(), name='new_student'),
    path('<str:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('<str:pk>/edit/', views.EditStudent.as_view(), name='edit_student'),
    path('<str:pk>/delete/', views.delete_student, name='delete_student'),
    path('api/', include(router.urls))
]