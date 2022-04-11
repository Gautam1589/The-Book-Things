from django.shortcuts import render
from .models import Feedback
from django.contrib import messages

# Create your views here.
def feedback(request):
    if request.method == 'POST':
        name = request.POST['nam']
        email = request.POST['email']
        rating = request.POST['rating']
        feedb = request.POST['fb']

        feedback = Feedback(name=name,email=email,feedback=feedb,rating=rating) 
        feedback.save()

        messages.success(request,"your feedback has been submitted.")
        return render(request,'home/home.html')
    
    else:
        return render(request,'feedback/feedback.html')

