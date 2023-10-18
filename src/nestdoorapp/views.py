from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *
from .forms import Memberform
# Create your views here.

def home_screen_view(request):
    return render(request, "homepage.html", {}) #<-- {} for database variables

def login_view(request):
    return render(request, "login.html", {}) #<-- {} for database variables

def logout_view(request):
    return render(request, "logout.html", {}) #<-- {} for database variables

def forum_view(request):
    return render(request, "forum.html", {}) #<-- {} for database variables

def about_view(request):
    return render(request, "about.html", {}) #<-- {} for database variables

def test_view(request):
    return render(request, "test.html", {})
    
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