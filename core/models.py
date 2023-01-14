from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')                   
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.message

class LikeMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')                   
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return self.user.username     
