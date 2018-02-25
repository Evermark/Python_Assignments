from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import Course

def index(request):
    context = {
    "courses": Course.objects.all()
    }
    return render(request, "courses_app/index.html", context)

def create(request):
    errors = Course.objects.course_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect("/courses")
    else:
        Course.objects.create(course_name = request.POST['course_name'],
            desc = request.POST['desc'])
        return redirect("/courses")

def show(request, course_id):
    context = {
    "course": Course.objects.get(id=course_id)
    }
    return render(request, 'courses_app/delete.html', context)

def delete(request, course_id):
    Course.objects.get(id=course_id).delete()
    return redirect('/courses')
