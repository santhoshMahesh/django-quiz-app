from xml.dom.domreg import registered
from django.http import HttpResponse
from quiz_app.forms import UserForm,questionsform
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import * 

def index(request):    
    return render(request,'quiz_app/index.html')

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

        if user:
            if user.is_active:
                login(request,user)
                Ques.objects.all().delete()
                return redirect('quizName')
            else:
    
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
       
        return render(request, 'quiz_app/login.html', {})

def quiz(request):
    if request.user.is_staff:
        form=questionsform()
        if(request.method=='POST'):
            form=questionsform(request.POST)
            if(form.is_valid()):
                form.save()
                form=questionsform()
                context={'form':form}
                return render(request,'quiz_app/quizName.html',context)
        context={'form':form}
        return render(request,'quiz_app/quizName.html',context)
    else: 
        return redirect('index') 

def takequiz(request):
    if request.method == 'POST':
        print(request.POST)
        questions=Ques.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            if q.ans==request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'quiz_app/results.html',context)
    else:
        questions=Ques.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'quiz_app/takequiz.html',context)

    

          







