#imports
from django.shortcuts import render, redirect
import uuid
# Create your views here.
def index(request):
    return render(request,'first_app/index.html')

def random(request, string_length=10):
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1

    str = uuid.uuid4().hex
    return render(request,'first_app/index.html')

def reset_session(request):
    request.session.clear()
    return redirect('/')
