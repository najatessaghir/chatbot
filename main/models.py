from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"Chat: {self.name} (User: {self.user.username})"

class Exchange(models.Model):
    question = models.CharField(max_length=200)
    response = models.TextField()
    # Change the relationship to ForeignKey to allow multiple Exchanges for one Chat
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='exchanges')

    def __str__(self):
        return f"Exchange: {self.question[:50]}... (Chat: {self.chat.name})"