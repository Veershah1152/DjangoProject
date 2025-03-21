from Demos.win32ts_logoff_disconnected import username
from django.shortcuts import render , redirect
from django.contrib.auth.models import User ,auth
from django.contrib import messages
# Create your views here.
def details(request):
    return render(request,'details.html')

def home(request):
    return render(request,'home.html')

def login(request):
     if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username , password = password)

        if user is not None:
            auth.login(request, user)
            return redirect("details")
        else:
            messages.info(request,'user not found')
            return redirect('login')

     else:
        return render(request,'login.html')

def register(request):
    if request.method =='POST':
      username =request.POST['username']
      email =request.POST['email']
      password1 =request.POST['password1']
      password2 =request.POST['password2']

      if password1==password2:
          if User.objects.filter(username=username).exists():
              messages.info(request,'User taken')
              return redirect('register')
          elif User.objects.filter(email=email).exists():
              messages.info(request, 'Email taken')
              return redirect('register')
          else:
           user = User.objects.create_user(username = username , password = password1 ,email = email)
           user.save()
           return redirect('login')
      else:
          messages.info(request, 'password not matching')
          return redirect('register')
      return redirect('/')
    else:
     return render(request,'register.html')