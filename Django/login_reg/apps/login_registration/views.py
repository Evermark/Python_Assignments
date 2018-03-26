from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *

def index(request):
    if "user_id" not in request.session:
        request.session["user_id"] = ""
    return render(request, "login_registration/index.html")

def registration(request):
    #create user in DB using reg_validator class
    errors = User.objects.reg_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        new_user = User.objects.create(first_name = request.POST["first_name"], last_name = request.POST["last_name"],
        email = request.POST["email"], password = request.POST["password"])

        request.session['first_name'] = new_user.first_name
        request.session['user_id'] = new_user.id
    return redirect ('/success')

def login(request):
    #login user via login_validator
    errors = User.objects.login_validator(request.POST)
    if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/')
    else:
        current_user = User.objects.get(email=request.POST["email"])
        request.session['user_id'] = current_user.id
        request.session['first_name'] = current_user.first_name

    return redirect ('/success')

def success(request):
    context = {
        "user": User.objects.get(id=request.session['user_id'])
    }
    return render(request, "login_registration/success.html", context)
