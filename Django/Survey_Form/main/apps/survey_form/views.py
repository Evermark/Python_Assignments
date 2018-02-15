from django.shortcuts import render, redirect, HttpResponse

def survey(request):
    return render(request, 'survey_form/input.html')

def process(request):
    request.session['Name'] = request.post['name']
    request.session['Dojo_Location'] = request.post['city']
    request.session['Language'] = request.post['language']
    request.session['Comments'] = request.post['comments']
    return redirect('/result')

def result(request):
    return render(request, '/survey_form/result.html')
# Create your views here.
