from home.models import posts
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import get_user_model

# Create your views here.

def home(request):
    posts_with_users = []
    for post in posts.objects.all():
        author = get_user_model().objects.get(pk=post.author_id)
        posts_with_users.append((post, author))
    context = {"posts_with_users": posts_with_users}
    return render(request, "home.html", context)



def register_user(request):

    if request.method == 'POST':
        firstName= request.POST.get('name')
        userName= request.POST.get('userName')

        user= User.objects.filter(username=userName)
        if user.exists():
            messages.info(request,"Username Already Exists")
            return redirect("registration")

        email=request.POST.get("email")
        password=request.POST.get("password")
        user=User.objects.create(first_name=firstName,username=userName,email=email)
        user.set_password(password)
        user.save()
        return redirect("/")
    return render(request,"register.html")

def login_user(request):
    if request.method == 'POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        if not(User.objects.filter(username=username).exists()):
            messages.info(request,"Invalid User Name ")
            return redirect("login")

        user=authenticate(username=username,password=password)

        if user is None:
            messages.info(request,"Invalid Password")
            return redirect("login")
        else:
            login(request,user)
            return redirect("/")
    return render(request,"login.html")

def account(request):

    if(request.user.is_authenticated):
        return render(request,"account.html")
    else:
        return redirect("login")


def logout_user(request):
    logout(request)
    return redirect('/')


def post(request):

    if(request.method=="POST"):
        poemName=request.POST.get("poemName")
        content=request.POST.get("content")
        user=request.user
        post=posts(poemName=poemName,content=content,author=user)
        post.save()
        return redirect("/")
    if(request.user.is_authenticated):
        return render(request, "post.html")
    else:
        return redirect("login")