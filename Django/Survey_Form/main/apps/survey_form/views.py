from django.shortcuts import render, redirect, HttpResponse

def survey(request):
    return render(request, 'survey_form/input.html')

def process(request):
    request.session['Name'] = request.POST['name']
    request.session['Dojo_Location'] = request.POST['city']
    request.session['Language'] = request.POST['language']
    request.session['Comments'] = request.POST['comments']
    return redirect('survey_form/result')

def result(request):
    return render(request, '/survey_form/result.html')
# Create your views here.
