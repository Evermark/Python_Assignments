from django.shortcuts import render, redirect

def index(request):
    return render(request, 'amadon/index.html')

def buy(request):
    print request.POST
    return redirect('/amadon')
    # return redirect('amandon/checkout')

def cart(request):
    return render(request, 'amadon/checkout.html')
