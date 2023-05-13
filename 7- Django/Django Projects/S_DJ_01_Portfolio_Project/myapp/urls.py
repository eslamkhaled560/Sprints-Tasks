from django.urls import path
from .views import student_list
from .views import course_list


urlpatterns = [
    path('students/', student_list, name='student_list'),
    path('courses/', course_list, name='courses_list'),
]
