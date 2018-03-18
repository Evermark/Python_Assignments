from django.shortcuts import render, redirect, HttpResponse
from time import localtime, strftime

def index(request):
    context = {
    "time": strftime("%b %d, %Y %H:%M %p", localtime())
    }
    return render(request,'time_display/index.html', context)
