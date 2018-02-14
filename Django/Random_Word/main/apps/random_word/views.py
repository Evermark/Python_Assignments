from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'attempt' not in request.session:
        request.session['attempt'] = 1
    else:
        request.session['attempt'] += 1
    random = {'word' : get_random_string(length=12)}
    return render(request, 'random_word/index.html', random)

def random_word(request):
    return redirect('/random_word')

def reset(request):
    request.session['attempt'] = 0
    return redirect('/random_word/reset')
