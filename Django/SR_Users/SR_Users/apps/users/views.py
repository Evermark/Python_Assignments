from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import User

def index(request):
    #create conditionals determine whether POSTing/GETing
    #form -> post request to (/users) -> redirect get(/users)
    if request.method == "POST":
        User.objects.create(name= request.POST['name'],
            email =request.POST ['email'])
        return redirect('users/new')
    elif request.method == "GET":
        # create dictionary to display values on index.html
        context = {
        "users": User.objects.all()
        }
    return render(request, "users/index.html", context)

def new(request):
    return render(request, 'users/add.html')

def edit(request, user_id):
    # create dictionary to display user info(values) in form
    context = {
        "user": User.objects.get(id=user_id)
    }
    return render(request, 'users/edit.html', context)
def destroy(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect('/users')
def show_or_update(request, user_id):
    if request.method == "POST":
        user = User.objects.get(id=user_id)
        # update name/email to name/email posted in form
        user.name = request.POST["name"]
        user.email = request.POST["email"]
        user.save()
        return redirect ("/users")
    else:
        context = {
        "user": User.objects.get(id=user_id)
        }
        return render(request, "users/show.html", context)
