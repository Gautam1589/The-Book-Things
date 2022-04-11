from django.shortcuts import render
from .models import BookDonation

# Create your views here.
def bookdonate(request):
    if request.method == 'POST':
        name = request.POST['nam']
        email = request.POST['email']
        mobile = request.POST['num']
        address = request.POST['addr']
        pincode = request.POST['pin']
        book = request.POST['bname']
        author = request.POST['aname']
        genre = request.POST['gname']
        pic = request.POST['fname']

        dbook = BookDonation(name=name,email=email,mobile=mobile,address=address,pincode=pincode,book=bookname,author=authorname,genre=genre,pic=img) 
        dbook.save()

        messages.success(request,"your feedback has been submitted.")
        return render(request,'home/home.html')
    else:
        return render(request,'donation/bookdonation.html')