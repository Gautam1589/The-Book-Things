from django.shortcuts import render
from .models import Book_details
from .models import Category
# Create your views here.
def collection(request):
    dests = Book_details.objects.all()
    cat=Category.objects.all()
    l=len(cat)
    cat1=Category.objects.all()[:l//2]
    cat2=Category.objects.all()[l//2:]

    context={
        'dests' : dests,
        'cat1' : cat1,
        'cat2' : cat2
    }
    return render(request,'collection/collection.html',context)