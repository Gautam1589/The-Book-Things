from django.db import models
from datetime import datetime

# Create your models here.
class BookDonation(models.Model):
    name=models.CharField(max_length=200,blank=True)
    email=models.CharField(max_length=200,blank=True)
    mobile=models.IntegerField(blank=True)
    address=models.TextField(blank=True)
    pincode=models.IntegerField(blank=True)
    bookname=models.CharField(max_length=200,blank=True)
    authorname=models.CharField(max_length=200,blank=True)
    genre=models.CharField(max_length=200,blank=True)
    img=models.ImageField(upload_to='donate/%Y/%m/%d/',blank=True)
    date=models.DateTimeField(default=datetime.now)
    

    def __str__(self):
        return self.name