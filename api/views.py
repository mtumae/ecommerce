from django.shortcuts import render
from .models import Item
from django.http import JsonResponse
from .forms import ItemForm
from django.contrib import messages

def example_view(request):
    return JsonResponse({'message': 'Mtume Owino Mutere'})





# Getters and Setters for Items
#-----------------------------------------------------------------------------
def getItems(request):
    items = Item.objects.all()
    items_list = list(items.values())
    return JsonResponse({'items':items_list})


def getItemsTest(request):
    items = Item.objects.all()
    items_list = list(items.values())
    return render(request, 'main/test.html', {'items':items})

def setItem(request):
    form = ItemForm(request.POST, request.FILES)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        form.save()
        messages.success(request, f"Item {name} has been saved")
    else:
        messages.error(request, f"Error!")
    

    return render(request, 'main/test.html', {'form':form})
    

        
    
       
       

        