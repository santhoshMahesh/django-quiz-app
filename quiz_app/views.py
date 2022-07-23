from django.http import HttpResponse
from quiz_app.forms import UserForm
from django.shortcuts import render
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    
    return render(request,'quiz_app/base.html')
# Create your views here.
def register(request):
    registered=False
    if request.method=="POST":
        user_form=UserForm(data=request.POST)

        if user_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            registered=True
        else:
            print(user_form.errors)
    else: 
        user_form=UserForm()

    return render(request,'quiz_app/register.html',{
         'registered':registered,
        'user_form':user_form
    })    
@login_required
def special(request):
  
    return HttpResponse("You are logged in. Nice!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('register'))

def user_login(request):
    
    if request.method == 'POST':
  
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
    
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
       
        return render(request, 'quiz_app/login.html', {})






