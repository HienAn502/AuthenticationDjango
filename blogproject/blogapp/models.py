from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.IntegerField(
        null=False, auto_created=True, primary_key=True
    )
    title = models.CharField(max_length=255)
    shortDesc = models.TextField()
    body = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)

