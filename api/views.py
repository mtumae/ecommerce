from django.shortcuts import render
from .models import Item
from django.http import JsonResponse

def example_view(request):
    return JsonResponse({'message': 'Mtume Owino Mutere'})


def getItems(request):
   items = Item.objects.all()
   return JsonResponse({items})