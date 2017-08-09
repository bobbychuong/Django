from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request,'survey/index.html')

def result_form(request):
    return render(request, 'survey/result.html')

def process_form(request):
    if 'times' not in request.session:
        request.session['times'] = 0
    else:
        request.session['times'] += 1
    request.session['name'] = request.POST['name']
    request.session['dojo_location'] = request.POST['dojo_location']
    request.session['fav_language'] = request.POST['fav_language']
    request.session['comment'] = request.POST['comment']
    return redirect('/result')
