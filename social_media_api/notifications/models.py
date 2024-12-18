from django.db import models
from django.conf import settings
# Create your models here.
class Notification(models.Model):
    recipient = models.ForeignKey(settings.Auth_User_Model, on_delete=models.CASCADE)
    actor = models.ForeignKey(settings.Auth_User_Model, on_delete=models.CASCADE)
    verb = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)