from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
# Create your views here.
def index(request):
    return HttpResponse("Working")


def example_view(request):
    return JsonResponse({'message': 'Mtume Owino Mutere'})