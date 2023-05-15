from django.shortcuts import redirect, render
from .models import Student, Course, Post
from .forms import PostForm


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})


def home_list(request):
    homes = Post.objects.all()
    return render(request, 'home_list.html', {'homes': homes})


def home(request):
    if request.method == 'POST':
        details = PostForm(request.POST)

        if details.is_valid():
            post = details.save(commit=False)
            post.save()
            return redirect('home_list')

        else:
            return render(request, "home.html", {'form': details})

    else:
        form = PostForm(None)
        return render(request, 'home.html', {'form': form})
