from django.shortcuts import render, redirect
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *
from .forms import Memberform, RegisterForm, UserAuthenticationForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.

def home_screen_view(request):
    return render(request, "homepage.html", {}) #<-- {} for database variables

def login_view(request):
    context = {}

    #Check if user is already logged in.
    user = request.user
    if user.is_authenticated:
        return redirect('home')

    #Check if requesting user login
    if request.method == "POST":
        form = UserAuthenticationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect('home')

    #Else normal user login page.
    else:
        form = UserAuthenticationForm()
    context['login_form'] = form
    return render(request, "registration/login.html", context) #<-- {} for database variables

def logout_view(request):
    logout(request)
    print("logged out")
    return redirect('home')
    #return render(request, "home.html", {}) #<-- {} for database variables

def forum_view(request):
    return render(request, "forum.html", {}) #<-- {} for database variables

def about_view(request):
    return render(request, "about.html", {}) #<-- {} for database variables

def password_reset(request):
    return render(request, 'registration/password_reset.html', {})

def password_reset_done(request):
    return render(request, 'registration/password_reset_done.html', {})


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/homepage')
    else:
        form = RegisterForm()
        
    return render(request, 'registration/sign_up.html', {"form":form})

#####Test_Views
def join(request):
    if request.method == "POST":
        form = Memberform(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'greeting.html')
    else:
        return render(request, 'greeting.html')


def name_list(request):
    all_members = Member.objects.all()
    return render(request, 'name_list.html', {'all': all_members})

class ReactView(APIView):
    
    serializer_class = ReactSerializer
  
    def get(self, request):
        detail = [ {"name": detail.name,"detail": detail.detail} 
        for detail in React.objects.all()]
        return Response(detail)
  
    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return  Response(serializer.data)
        
