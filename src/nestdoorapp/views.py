from . models import *
from . serializer import *
from .forms import Memberform, RegisterForm, UserAuthenticationForm, PostCreationForm
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

def home_screen_view(request):
    context = {}
    context["your_id"] = request.user.id
    return render(request, "homepage.html", context) #<-- {} for database variables

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
    context = {}
    # Pass in post objects for display
    posts = Post.objects.all()
    context['posts'] = posts
    context["your_id"] = request.user.id

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
            obj.posted_by = user
            obj.save()
            form = PostCreationForm(request.GET)
            context['post_form'] = form
            return render(request, 'forum.html', context)
        else:
            print("form not valid")
    context['post_form'] = form
    return render(request, "forum.html", context) #<-- {} for database variables

def about_view(request):
    context = {}
    context["your_id"] = request.user.id
    return render(request, "about.html", context ) #<-- {} for database variables

def user_post_view(request):
    context = {}
    post_id = request.GET.get('postid', 1) # ID num will we passed in... 1 is default
    post = Post.objects.filter(post_id=post_id)[0]
    replies = Reply.objects.filter(for_post_id=post_id)
    context['post'] = post
    context['replies'] = replies
    context["your_id"] = request.user.id
    # id = request.POST.get('id', '200') #Gets the post id from the post request from the Forum. 200 is just a default random value in case id does not exist
    # try:
    #     Post.objects.filter(post_id=id)[0] #Checks if the id from the url is equals to any post_id from the database and grabs the first value
    # except:
    #     print("An error occured with post_id")
    # context = {'Post':Post} #Passes that first value (the post id) to the context
    return render(request, "userpost.html", context) #<-- {} for database variables

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

def edit_post(request):
    context = {"has_no_err": True}
    context["your_id"] = request.user.id
    if request.method == "GET":
        post_id = request.GET.get("post", None)
        if post_id != None:
            post = Post.objects.get(post_id__exact=post_id)
            if post.posted_by == request.user:
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
            if post.posted_by == request.user:
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


def bad_profile_view(request):
    context = {}
    context["your_id"] = request.user.id
    return render(request, "bad_user.html", context)

def user_profile_view(request, user_id):
    context = {}
    context["is_me"] = request.user.id == user_id
    
    try:
        user = User.objects.get(id = user_id)
    except ObjectDoesNotExist:
        return render(request, "bad_user.html")

    # get about_me and update if this is a post
    try:
        user_ext = UserExt.objects.get(user = user)
        # check if this is a post and user has permission to post
        if request.method =='POST' and request.user.id == user_id:
            user_ext.about_me = request.POST["about_me"]
            user_ext.save()
        context["about_me"] = user_ext.about_me
    # if the UserExt object has not yet been created
    except ObjectDoesNotExist:
        # check if this is a post and user has permission to post
        if request.method =='POST' and request.user.id == user_id:
            user_ext = UserExt()
            user_ext.user = user
            user_ext.about_me = request.POST["about_me"]
            user_ext.save()
            context["about_me"] = user_ext.about_me    
        else:
            # default about me
            context["about_me"] = "This user has not filled out this about me yet."
        

    # build context variables
    context["username"] = user.username.upper()
    context["num_posts"] = Post.objects.filter(posted_by = user_id).count()
    context["num_comments"] = Reply.objects.filter(posted_by = user_id).count()
    context["your_id"] = request.user.id
    return render(request, "userprofilepage.html", context)

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
        