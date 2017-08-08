from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

# Create your views here.
def index(request):
    context = {
    "time":strftime("%b %m, %Y", gmtime()),
    "timeofday":strftime("%I %M %S", gmtime())
    }
    return render(request, "time_display/index.html", context)
