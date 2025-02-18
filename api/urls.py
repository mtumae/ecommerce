from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('example/', views.example_view, name='example'),
    path('items/',views.getItems, name='items' ),
    path('setItems/', views.setItem, name='setItem'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)