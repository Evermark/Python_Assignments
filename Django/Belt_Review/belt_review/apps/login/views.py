from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages


def index(request):
    if "user_id" not in request.session:
        request.session["user_id"] = ""
    return render(request, 'login/index.html')

def register(request):
    errors = User.objects.reg_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        new_user = User.objects.create(name = request.POST["name"], alias = request.POST["alias"], email=request.POST["email"], password = request.POST["password"] )
        request.session['name'] = new_user.name
        request.session['user_id'] = new_user.id
    return redirect('/books')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        current_user = User.objects.get(email=request.POST["email"])
        request.session['name'] = new_user.name
        request.session['user_id'] = new_user.id
    return redirect('/books')
