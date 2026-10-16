from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.

from .forms import CourseForm
from .models import Course

def course_list(request):
    courses = Course.objects.all()
    return render(request,"courses/course_list.html",{"courses":courses})

def course_detail(request,pk):
    course = get_object_or_404(Course,pk=pk)
    return render(request,"courses/course_detail.html",{"course":course})

@login_required
def dashboard(request):
    return render(request,"courses/dashboard.html")

def course_create(request):
    if(request.method =="POST"):
        form = CourseForm(request.POST)
        if(form.is_valid()):
            form.save()
    else :
        form = CourseForm()
    return render(request,"courses/course_form.html",{"form":form})
        
