from django.shortcuts import render, redirect
from datetime import datetime


def index(request):
    return render(request, 'session_words/words.html')

def add_words(request):
    # create table
    if 'info' not in request.session:
        request.session.['info'] = []
    new_words = {
        'word': request.POST['word']
        'color': request.POST['color']
        'time': datetime.now().strftime("%b %d, %Y %H:%M %p")
    }
    # set variable for font size checkbox
    try:
        request.POST['big']
        new_words['big'] = 'on'
    except:
        pass
    if 'big' not in request.POST:
        new_word['big'] = 'off'
    else:
        new_word['big'] = 'on'
    request.session['info'].append(new_words)
    request.session['word'] = request.POST['word']
    # request.session['color'] = request.POST['color']
    # request.session['size'] = request.POST['size']
    return redirect('/session_words')

def clear(request):
    request.session.clear()
    return redirect('/session_words')
