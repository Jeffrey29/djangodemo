from django import forms
from .models import Course, Student

class NewStudentForm(forms.ModelForm):
    z_id = forms.CharField(max_length=8)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Student 
        fields = ['z_id', 'first_name', 'last_name', 'courses']
        
class EditStudentForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Student 
        fields = ['first_name', 'last_name', 'courses']