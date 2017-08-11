from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
        request.session
        request.session['count']
        if 'count' in request.session:
            request.session['count'] += 1

        return render(request,'first_app/index.html')
