from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'yourapp/index.html')

def about(request):
    return render(request, 'yourapp/about.html')

def projects(request):
    return render(request, 'yourapp/projects.html')

def testimonials(request):
    return render(request, 'yourapp/testimonials.html')
