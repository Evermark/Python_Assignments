from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
import random

def index(request):
    if 'gold' not in request.session:
        request.session['gold']= 0
    if 'ninja_wins' not in request.session:
        request.session['ninja_wins'] = []
    if 'ninja_losses' not in request.session:
        request.session['ninja_losses'] = []
    context = {
        "gold": request.session['gold'],
        "wins": request.session['ninja_wins'],
        "losses": request.session['ninja_losses']
    }
    return render(request, "ninja_gold/index.html", context)

def process_money(request):
    time = datetime.now().strftime("%b %d, %Y %H:%M %p")
    if request.POST['building'] == "farm":
        request.session['farm']= random.randint(10,20)
        request.session['gold'] += request.session['farm']
        request.session['ninja_wins'].append('Earned '+str(request.session['farm'])+ " gold from farm. " +str(time))
    elif request.POST['building'] == "cave":
        request.session['cave']= random.randint(5,10)
        request.session['gold'] += request.session['cave']
        request.session['ninja_wins'].append('Earned '+str(request.session['cave'])+ " gold from cave. " +str(time))
    elif request.POST['building'] == "house":
        request.session['house']= random.randint(2,5)
        request.session['gold'] += request.session['house']
        request.session['ninja_wins'].append('Earned '+str(request.session['house'])+ " gold from house. " +str(time))
    elif request.POST['building'] == "casino":
        request.session['casino']= random.randint(-50,50)
        if request.session['casino']< 0:
            request.session['ninja_losses'].append('Entered a casino and lost ' +str(request.session['casino'])+" gold. Yikes! " +str(time))
        else:
            request.session['gold'] += request.session['casino']
            request.session['ninja_wins'].append('Entered a casino and won '+str(request.session['casino'])+ " gold from casino! " +str(time))

    return redirect('/ninja_gold')
