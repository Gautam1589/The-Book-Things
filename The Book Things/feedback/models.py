from django.db import models

# Create your models here.
class Feedback(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    feedback=models.TextField()
    rating=models.IntegerField(default=0)

    def __str__(self):
        return self.name