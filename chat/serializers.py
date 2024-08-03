from rest_framework import serializers
from .models import Chats, Room, AdminRoom

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class ChatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chats
        fields = '__all__'
        
class ARSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminRoom
        fields = '__all__'