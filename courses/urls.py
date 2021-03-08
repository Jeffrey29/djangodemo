from django.urls import path

from . import views 

app_name = 'courses'

urlpatterns = [
    path('students/', views.AllStudentsView.as_view(), name='all_students'),
    path('new-student/', views.NewStudent.as_view(), name='new_student'),
    path('<str:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('<str:pk>/edit/', views.EditStudent.as_view(), name='edit_student'),
    path('<str:pk>/delete/', views.delete_student, name='delete_student')
]