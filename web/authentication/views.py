from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login

# Create your views here.
def home(request):
    return render(request,"authentication/index.html")
def signup(request):
    if request.method =="POST":
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        #stid=request.POST['stid']
        #password1=request.POST['password1']
        #ConfirmPassword=request.POST['ConfirmPassword']

        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()

        messages.success(request,"Your Account has been Successfully Created.")

        return redirect("signin")
    


    return render(request,"authentication/signup.html")
def signin(request):
    if request.method =="POST":
        username=request.POST['username']
        pass1=request.POST['pass1']
        user= authenticate(username=username,password=pass1)

        if user is not None:
            login(request,user)
            fname=user
            return render(request,"authentication/index.html",{"fname":fname})
        else:
            messages.error(request,"Worong Password")
            return redirect('home')
    return render(request,"authentication/signin.html")
def signout(request):
    pass
