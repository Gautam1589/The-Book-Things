from django.shortcuts import render
from collection.models import Book_details
from collection.models import Category
from .models import Book_rating
from django.contrib import messages
# Create your views here.
def oneview(request,view_id):
    book_view=Book_details.objects.get(id=view_id)
    brat=Book_rating.objects.filter(book_id=view_id)
    cat=Category.objects.all()
    l=len(cat)
    cat1=Category.objects.all()[:l//2]
    cat2=Category.objects.all()[l//2:]
    l=list(brat)
    s=0
    for i in l:
        t=i.rating
        s=s+t
    
    if len(l)!=0:
        b=s/len(l)   
    else:
        b=0

    context={
        'book_view': book_view,
        'br' : b,
        'cat' : cat,
        'cat1' : cat1,
        'cat2' : cat2
        }
    return render(request,'book_disp/display.html',context)

def bookrating(request,view_id):
    if request.method == 'POST':
        b_id = view_id
        rating = request.POST['rating']

        bookrating = Book_rating(rating=rating,book_id=b_id) 
        bookrating.save()

        messages.success(request,"your rating has been submitted")
        return render(request,'home/home.html')
    
    else:
        return render(request,'book_disp/display.html')