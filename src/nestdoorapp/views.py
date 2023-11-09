from django.shortcuts import render, redirect
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *
from .forms import Memberform, RegisterForm, UserAuthenticationForm, PostCreationForm
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
    return redirect(home)
    #return render(request, "home.html", {}) #<-- {} for database variables

def forum_view(request):
    context = {}
    # Pass in post objects for display
    posts = Post.objects.all()
    context['posts'] = posts

    #Default request GET
    if request.method == "GET":
        form = PostCreationForm(request.GET)

    #If request post, user trying to submit a post
    if request.method == "POST":
        user = request.user
        form = PostCreationForm(request.POST)
        if form.is_valid():
            print("valid form")
            obj = form.save(commit=False)
            obj.author = user
            obj.save()
            form = PostCreationForm(request.GET)
            context['post_form'] = form
            return render(request, 'forum.html', context)
        else:
            print("form not valid")
    context['post_form'] = form
    return render(request, "forum.html", context) #<-- {} for database variables

def about_view(request):
    return render(request, "about.html", {}) #<-- {} for database variables

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

def edit_post(request):
    context = {"has_no_err": True}
    if request.method == "GET":
        post_id = request.GET.get("post", None)
        if post_id != None:
            post = Post.objects.get(post_id__exact=post_id)
            if post.author == request.user:
                context["post"] = post
                return render(request, "post_edit.html", context)
            else:
                context["has_no_err"] = False
                context["err_msg"] = "Logged in user does not match post author"
                return render(request, "post_edit.html", context)
        else:
            context["has_no_err"] = False
            context["err_msg"] = "Invalid request (missing post)"
            return render(request, "post_edit.html", context)
    else:
        post_id = request.POST.get("post_id", None)
        new_content = request.POST.get("edit_content", None)
        if post_id != None and new_content != None:
            post = Post.objects.get(post_id__exact=post_id)
            if post.author == request.user:
                post.content = new_content
                post.save()
                return redirect("/userpost?postid=" + str(post_id))
            else:
                context["has_no_err"] = False
                context["err_msg"] = "Logged in user does not match post author"
                return render(request, "post_edit.html", context)
        else:
            context["has_no_err"] = False
            context["err_msg"] = "Invalid request (missing post_id or edit_context)"
            return render(request, "post_edit.html", context)



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
        
