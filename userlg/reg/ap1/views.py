from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def homepage(req):
    return render (req,'home.html')
 

def signuppage(req):
    if req.method=='POST':
        uname=req.POST.get('username')
        email=req.POST.get('email')
        pass1=req.POST.get('password1')
        pass2=req.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("ur password doesnt match")

        else:
            myuser=User.objects.create_user(uname,email,pass1)
            myuser.save()
            return redirect('login')

    return render (req,'signup.html')


def loginpage(req):
    if req.method=='POST':
        username=req.POST.get('username')
        pass1=req.POST.get('pass')
        print(username,pass1)
        user=authenticate(req,username=username,password=pass1)
        if user is not None:
            login(req,user)
            return redirect('home')
        else:
            return HttpResponse("username and password doesnt match")



    return render (req,'login.html')



def logoutpage(req):
    logout(req)
    return redirect('login')
