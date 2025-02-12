from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Apparel site made by mtume & kelvin")