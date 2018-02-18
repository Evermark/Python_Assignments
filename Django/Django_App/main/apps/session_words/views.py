from django.shortcuts import render, redirect
from datetime import datetime

now = datetime.now()

def index(request):
    return render(request, 'session_words/words.html')

def add_words(request):
    request.session['word'] = request.post['word']
    request.session['color'] = request.post['color']
    request.session['size'] = request.post['size']
    context = {
    "time": now.strftime("%b %d, %Y %H:%M %p")}
    return redirect('/session_words')

def clear(request):
    request.session['word'] = ''
    request.session['color'] = ''
    request.session['size'] = ''
    return render(request, 'session_words/words.html')
