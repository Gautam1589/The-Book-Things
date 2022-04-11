from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from collection.models import Category

# Create your views here.
def register(request):
    cat=Category.objects.all()
    l=len(cat)
    cat1=Category.objects.all()[:l//2]
    cat2=Category.objects.all()[l//2:]

    context2= {
        'cat1': cat1,
        'cat2': cat2

    }
    if request.method=='POST':
        fname = request.POST['fnam']
        lname = request.POST['lnam']
        uname = request.POST['unam']
        email = request.POST['email']
        password = request.POST['pass']
        cpassword = request.POST['cpass']

        if password==cpassword:
            if User.objects.filter(username=uname).exists():
                messages.error(request,'username already exists')
                return redirect('register')

            elif User.objects.filter(email=email).exists():  
                messages.error(request,'email already exists')
                return redirect('register')

            else:     
                user = User.objects.create_user(username=uname,email=email,password=password,first_name=fname,last_name=lname)
                user.save()
                messages.success(request,'user registered successfully')
                return redirect('login')

        else:
            messages.error(request,'password do not match')
            return render(request,'accounts/register.html')
    else:
        return render(request,'accounts/register.html',context2)

def login(request):
    cat=Category.objects.all()
    l=len(cat)
    cat1=Category.objects.all()[:l//2]
    cat2=Category.objects.all()[l//2:]

    context2= {
        'cat1': cat1,
        'cat2': cat2

    }
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['pass']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.error(request,'Invalid credentials')
            return redirect('login')    


    else:
        return render(request,'accounts/login.html',context2)
    
def logout(request):
    auth.logout(request)
    messages.success(request,'logout sucessfully')
    return redirect('/')    
