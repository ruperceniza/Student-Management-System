from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'course', 'gender', 'age']
        widgets = {
            'gender': forms.RadioSelect
        }

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['gender'].empty_label = None

class FilterForm(forms.Form):
    full_name = forms.CharField(required=False, label='Search by Full Name')
    course = forms.ChoiceField(choices=[
        ('', '--------'),
        ('BS-CS', 'Computer Science'),
        ('BS-DS', 'Data Science'),
        ('BS-IT', 'Information Technology'),
        ('BS-IS', 'Information Systems')
    ], required=False)
    gender = forms.ChoiceField(choices=[
        ('', '--------'),
        ('Male', 'Male'),
        ('Female', 'Female')
    ], required=False)
    age_min = forms.IntegerField(required=False, label='Minimum Age')
    age_max = forms.IntegerField(required=False, label='Maximum Age')