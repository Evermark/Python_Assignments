from django.shortcuts import render, redirect
from datetime import datetime

def index(request):
    return render(request, 'session_words/words.html')

def add_words(request):
    #create new list
    if not 'info' in request.session:
        request.session['info'] = []
    new_words = {
        'word': request.POST['word'],
        'color': request.POST['color'],
        'time':datetime.now().strftime("%b %d, %Y %H:%M %p" )
    }

    request.session['info'].append(new_words)
    request.session['word'] = request.POST['word']
    request.session['color'] = request.POST['color']
    print new_words
    print request.session['info']
    return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')
