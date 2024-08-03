from django.db import models

class Room(models.Model):
    user_id = models.CharField(max_length=250)
    is_unread_user = models.BooleanField(default=False)
    is_unread_admin = models.BooleanField(default=False)
    is_user_active = models.BooleanField(default=False)
    is_admin_active = models.BooleanField(default=False)
    user_lastactive = models.DateTimeField(blank=True, null=True)
    admin_lastactive = models.DateTimeField(blank=True, null=True)
    last_message = models.TextField(blank=True, null=True)
    is_user_typing = models.BooleanField(default=False, null=True)
    is_admin_typing = models.BooleanField(default=False, null=True)

class Chats(models.Model):
    room = models.CharField(max_length=250)
    message = models.TextField(blank=True, null=True)
    role=models.CharField(max_length=250, default="user")
    message_type = models.CharField(max_length=100, default="text")
    created_at = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)
    seen_time_stamp = models.CharField(max_length=250, blank=True)
    
class AdminRoom(models.Model):
    room=models.CharField(max_length=250, blank=True)
    
    def __str__(self):
        return self.room