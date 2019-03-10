from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Event(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateTimeField()
    incoming_participants = models.ManyToManyField(User, related_name='incoming_participants', blank=True)

    def __str__(self):
        return self.title
