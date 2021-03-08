from django.urls import path

from . import views 

app_name = 'courses'

urlpatterns = [
    path('students/', views.AllStudentsView.as_view(), name='all_students'),
    path('new-student/', views.NewStudent.as_view(), {'type': 'add'}, name='new_student'),
    path('<str:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('<str:pk>/edit/', views.EditStudent.as_view(), {'type': 'edit'}, name='edit_student'),
    path('<str:pk>/delete/', views.delete_student, name='delete_student')
]