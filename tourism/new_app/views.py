from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    return render(request,'login.html')



def function(request):
    if request.method == 'POST':
        username = request.POST['username']
        first = request.POST['firstname']
        last = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['confirm_password']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already exist')
                return redirect('/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exist')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=first,last_name=last,email=email,password=password)

                user.save();
                return redirect(request,'login')


        else:
            messages.info(request,'password not matching')
            return redirect('register')
        return redirect('/')
    return render(request,'registration.html')
def logout(request):
    auth.logout(request)
    return redirect('/')