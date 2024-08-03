# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('chats/<int:pk>/', views.chats, name='chats'), 
    path('rooms/', views.rooms, name='rooms'), 
]
