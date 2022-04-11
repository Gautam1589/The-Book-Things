from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail 
from .models import Contact
from django.conf import settings
from collection.models import Category
from django.template.loader import get_template

# Create your views here.
def contact(request): 
    cat=Category.objects.all()
    l=len(cat)
    cat1=Category.objects.all()[:l//2]
    cat2=Category.objects.all()[l//2:]

    context2= {
        'cat1': cat1,
        'cat2': cat2

    }

    if request.method == 'POST':
        name = request.POST['nam']
        email = request.POST['email']
        message = request.POST['issue']


        contact = Contact(name=name,email=email,message=message) 
        contact.save()
        
        

        context = {
            'name': name,
            'email': email,
            'message': message
        }
        context1= {
            'name': name
        } 

        txt_ = get_template('contact/emails/contact-form.txt').render(context)
        from_email = settings.DEFAULT_FROM_EMAIL


        send_mail(
            'Enquiry sent from TheBookThings',
            txt_,
            from_email,
            ['gautamyadav1515@gmail.com'],
            fail_silently=False
        )
     
        
        messages.success(request,"your request has been submitted, a realtor will get back to you")
        return render(request,'contact/contact.html',context1)

    else:
        return render(request,'contact/contact.html',context2)

# def contact1(request):
#     cat=Category.objects.all()
#     l=len(cat)
#     cat1=Category.objects.all()[:l//2]
#     cat2=Category.objects.all()[l//2:]
#     context= {
#             'cat1' : cat1,
#             'cat2' : cat2
#         }

#     return render(request,'contact/contact.html',context)    