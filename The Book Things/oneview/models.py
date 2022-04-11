from django.db import models

# Create your models here.
class Book_rating(models.Model):
    book_id=models.IntegerField()
    rating=models.IntegerField(default=0)

    def __str__(self):
        return str(self.book_id)