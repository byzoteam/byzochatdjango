from django.contrib import admin
from .models import Chats, Room, AdminRoom
# Register your models here.

admin.site.register(Chats)
admin.site.register(Room)
admin.site.register(AdminRoom)