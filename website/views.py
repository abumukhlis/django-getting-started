from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse


def welcome(request):
    return render(request, "website/welcome.html",
                  {"message": "This data was sent from the view to the template."})


def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))


def about(request):
    return HttpResponse("This page is all about me.\n I am Azeez Lawal, a fullstack developer")

