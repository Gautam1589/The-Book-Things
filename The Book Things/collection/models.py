from django.db import models

# Create your models here.
class Category(models.Model):
    catname=models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.catname

class Book_details(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)     
    name=models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    auther= models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='pics')
    purchase_link = models.URLField(max_length=500,blank=True)
    bestseller= models.BooleanField(default=False)
    bestforchildren = models.BooleanField(default=False)

    
    def __str__(self):
        return self.name