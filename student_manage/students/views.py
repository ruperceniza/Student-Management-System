from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from .forms import FilterForm
from django.urls import reverse

def student_list(request):
    if request.method == 'GET':
        form = FilterForm(request.GET)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            course = form.cleaned_data['course']
            gender = form.cleaned_data['gender']
            age_min = form.cleaned_data['age_min']
            age_max = form.cleaned_data['age_max']

            students = Student.objects.all()

            if full_name:
                students = students.filter(first_name__icontains=full_name) | students.filter(last_name__icontains=full_name)
            if course:
                students = students.filter(course=course)
            if gender:
                students = students.filter(gender=gender)
            if age_min is not None:
                students = students.filter(age__gte=age_min)
            if age_max is not None:
                students = students.filter(age__lte=age_max)
    else:
        form = FilterForm()
        students = Student.objects.all()

    return render(request, 'students/student_list.html', {'form': form, 'students': students})

def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {'form': form})

def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('/')


from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

def update_student(request, student_id):
    if request.method == 'POST':
        student = get_object_or_404(Student, id=student_id)
        student.first_name = request.POST.get('full_name', '').split(' ')[0]
        student.last_name = request.POST.get('full_name', '').split(' ')[1] if len(request.POST.get('full_name', '').split(' ')) > 1 else ''
        student.course = request.POST.get('course', '')
        student.gender = request.POST.get('gender', '')
        student.age = request.POST.get('age', 0)
        student.save()
        return redirect(reverse('student_list'))
    return redirect(reverse('student_list'))