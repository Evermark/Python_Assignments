from django.shortcuts import render, redirect
from datetime import datetime

now = datetime.now()

def index(request):
    return render(request, 'session_words/words.html')

def add_words(request):
    print 'got word'
    request.session['word'] = request.POST['word']
    # request.session['color'] = request.POST['color']
    # request.session['size'] = request.POST['size']
    context = {
    "time": datetime.now().strftime("%b %d, %Y %H:%M %p")}
    return redirect('/session_words')

def clear(request):
    request.session.clear()
    return redirect('/session_words')
