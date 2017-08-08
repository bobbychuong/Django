from django.shortcuts import render,redirect
VALUES = ['populate this list with various strings']
# Create your views here.
def index(request):
    return render(request, "surprise/index.html")

def results(request):
    return render(request, "surprise/results.html")
