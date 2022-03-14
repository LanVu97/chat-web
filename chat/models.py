from account.models import Profile
from django.db import models

# Create your models here.


class Message(models.Model):
     sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender_mess')        
     receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver_mess')        
     message = models.CharField(max_length=1200)
     timestamp = models.DateTimeField(auto_now_add=True)
     seen = models.BooleanField(default=False)
     def __str__(self):
           return self.message
     class Meta:
           ordering = ('timestamp',)