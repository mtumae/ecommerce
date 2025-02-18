from django.urls import path
from . import views

urlpatterns = [
    path('example/', views.example_view, name='example'),
    path('products/', views.getItems, name='products'	)
]