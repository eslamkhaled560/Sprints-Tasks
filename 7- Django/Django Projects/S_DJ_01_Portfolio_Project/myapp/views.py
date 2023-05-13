from django.shortcuts import render

# Create your views here.
from .models import Student, Course


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})
