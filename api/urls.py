from django.urls import path
from . import views

urlpatterns = [
    path('example/', views.example_view, name='example'),
    path('items/',views.getItems, name='items' ),
    path('itemstest/',views.getItemsTest, name='itemstest' ),
    path('setItems/',views.setItem, name='setItem' )

]