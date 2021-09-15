from django.db import models
from django.utils.timezone import now
# Create your models here.
class feedback(models.Model):
    name=models.CharField(max_length=150)
    date=models.DateTimeField(default=now)
    suggestion=models.TextField()
    rating=models.IntegerField()

    def __str__(self):
        return self.name
