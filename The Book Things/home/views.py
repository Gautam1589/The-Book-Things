from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
from collection.models import Book_details
from collection.models import Category


def home(request):
    #return HttpResponse("hello...my website")
    info=Book_details.objects.all()[:8]
    cat=Category.objects.all()
    l=len(cat)
    cat1=Category.objects.all()[:l//2]
    cat2=Category.objects.all()[l//2:]
    # print(cat1)
    # print(cat2)
    

    context={
        'info' : info,
        'cat' : cat,
        'cat1' : cat1,
        'cat2' : cat2
    }
    return render(request,'home/home.html',context)

def catfun(request,cate):
    info=Category.objects.get(catname=cate)
    infohorror=info.book_details_set.all()
    cat=Category.objects.all()
    l=len(cat)
    cat1=Category.objects.all()[:l//2]
    cat2=Category.objects.all()[l//2:]


    context={
        'infohorror' : infohorror,
        'cat1' : cat1,
        'cat2' : cat2,
        'categ' : cate
    }
    return render(request,'categories/horror.html',context)

# def oneview(request):
    
#     return render(request,'book_desp/display.html')