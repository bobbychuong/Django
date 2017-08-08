#imports
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
import random
import string

# Create your views here.
def index(request):

    return render(request,'first_app/index.html')


def random(request):
    unique_id = get_random_string(length=10)
    if 'count' in request.session:
        request.session['count'] += 1
        request.session['word'] = unique_id
    else:
        request.session['count'] = 1
        request.session['word'] = unique_id
    return render(request,'first_app/index.html')


def reset_session(request):
    request.session.clear()
    return redirect('/')
