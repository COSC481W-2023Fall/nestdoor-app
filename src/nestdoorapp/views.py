from . models import *
from . serializer import *
from .forms import Memberform, RegisterForm, UserAuthenticationForm
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


def home_screen_view(request):
    context = {}
    context["your_id"] = request.user.id
    # <-- {} for database variables
    return render(request, "homepage.html", context)


def login_view(request):
    context = {}

    # Check if user is already logged in.
    user = request.user
    if user.is_authenticated:
        return redirect('home')

    # Check if requesting user login
    if request.method == "POST":
        form = UserAuthenticationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect('home')

    # Else normal user login page.
    else:
        form = UserAuthenticationForm()
    context['login_form'] = form
    # <-- {} for database variables
    return render(request, "registration/login.html", context)


def logout_view(request):
    logout(request)
    print("logged out")
    return redirect('home')
    # return render(request, "home.html", {}) #<-- {} for database variables


def forum_view(request):
    context = {}
    context["your_id"] = request.user.id
    # <-- {} for database variables
    return render(request, "forum.html", context)


def about_view(request):
    context = {}
    context["your_id"] = request.user.id
    # <-- {} for database variables
    return render(request, "about.html", context)


# lu
def user_post_view(request, pk):
    post = Post.objects.get(post_id=pk)

    comments = post.reply_set.all()

    if request.method == 'POST':
        comment = Reply.objects.create(
            posted_by=request.user,
            for_post_id=post,
            content=request.POST.get('body')
        )
        return redirect('user_post', pk=post_id)

    context = {'post': post, 'comments': comments}
    return render(request, 'userpost.html', context)


# def user_post_view(request):
#     context = {}
    # ID num will we passed in... 1 is default
    # post_id = request.GET.get('postid', '1')
    # post = Post.objects.filter(post_id=post_id)[0]
    # replies = Reply.objects.filter(for_post_id=post_id)
    # context['post'] = post
    # context['replies'] = replies
    # context["your_id"] = request.user.id

    # id = request.POST.get('id', '200') #Gets the post id from the post request from the Forum. 200 is just a default random value in case id does not exist
    # try:
    #     Post.objects.filter(post_id=id)[0] #Checks if the id from the url is equals to any post_id from the database and grabs the first value
    # except:
    #     print("An error occured with post_id")
    # context = {'Post':Post} #Passes that first value (the post id) to the context
    # <-- {} for database variables

    # return render(request, "userpost.html", context)


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/homepage')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})


def bad_profile_view(request):
    context = {}
    context["your_id"] = request.user.id
    return render(request, "bad_user.html", context)


def user_profile_view(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except ObjectDoesNotExist:
        return render(request, "bad_user.html")
    context = {}
    context["is_me"] = request.user.id == user_id
    context["username"] = user.username.upper()
    context["num_posts"] = Post.objects.filter(posted_by=user_id).count()
    context["num_comments"] = Reply.objects.filter(posted_by=user_id).count()
    context["your_id"] = request.user.id
    return render(request, "userprofilepage.html", context)

# Test_Views


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
        detail = [{"name": detail.name, "detail": detail.detail}
                  for detail in React.objects.all()]
        return Response(detail)

    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
