from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'session_words/index.html')

def add_word(request):
    new_word = {}
    

    # new_word['big'] = ''
    # request.session['words'] = []
    # temp_list = request.session['words']
    # temp_list.append(new_word)
    # request.session['words'] = temp_list
    return redirect('/')
