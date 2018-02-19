from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return HttpResponse('placeholder for users to create a new user record')

def login(request):
    return HttpResponse('placeholder for users to login')

def users(request):
    return HttpResponse('placeholder to later display all the list of users')

# Create your views here.
