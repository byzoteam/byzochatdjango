from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import *
from .serializers import *


@api_view(['GET'])
def chats(request, pk):
  chats = Chats.objects.filter(room=pk)
  data = ChatsSerializer(chats, many=True)
  return Response(data.data, status=status.HTTP_200_OK)



@api_view(['GET'])
def rooms(request):
  chats = Room.objects.all()
  data = RoomSerializer(chats, many=True)
  return Response(data.data, status=status.HTTP_200_OK)
 


