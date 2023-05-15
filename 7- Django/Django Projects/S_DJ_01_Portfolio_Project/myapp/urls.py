from django.urls import path
from .views import student_list, course_list, home, home_list


urlpatterns = [
    path('students/', student_list, name='student_list'),
    path('courses/', course_list, name='courses_list'),
    path('home/', home, name='home'),
    path('home_list/', home_list, name='home_list'),
]
