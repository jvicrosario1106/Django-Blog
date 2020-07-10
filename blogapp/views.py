from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm,CategoryForm,AuthorForm,UserForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .decorators import isauthentication,allowed
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.

@login_required(login_url = "login_user")
def home(request):

    post = Post.objects.order_by("-date_created")[0:3]

    content = {

        "post":post

    }

    return render(request, "blogapp/home.html",content)


def projects(request):
    post = Post.objects.all()
    paginator = Paginator(post,1)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)

    except PageNotAnInteger:
        posts = paginator.page(1)
    
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    content = {
        "posts":posts
    }
    return render(request, 'blogapp/project.html',content)










# THIS SECTION IS FOR AUTHENTICATION
@isauthentication
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username = username, password = password)

        if user is not None:
            login(request,user)
            return redirect("home")

        else:
            return redirect("login_user")

    return render(request, "blogapp/login.html")


def logout_user(request):
    logout(request)
    return redirect("login_user")



def register(request):
    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_user")

    else:
        form = UserForm()

    content = {
        "form":form
    }

    return render(request, "blogapp/registration.html", content )

#-----------------------------------------------------------



























# THIS SECTION IS FOR ADMIN ONLY

@login_required(login_url = "login_user")
@allowed(allowed_roles=["admin"])
def addpost(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")

    content = {
        "form":form
    }

    return render(request, 'blogapp/addpost.html',content)


@login_required(login_url = "login_user")
@allowed(allowed_roles=["admin"])
def addcat(request):
    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    content = {
        "form":form
    }

    return render(request, 'blogapp/addcat.html',content)

@login_required(login_url = "login_user")
@allowed(allowed_roles=["admin"])
def addauthor(request):
    form = AuthorForm()
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    content = {
        "form":form
    }

    return render(request, 'blogapp/addauthor.html',content)


@allowed(allowed_roles=['admin'])
def updatepost(request,pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)

    if request.method == "POST":
        form  = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("home")

    content = {
        "form":form
    }

    return render(request, "blogapp/updatepost.html",content)


def deletepost(request,pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect("home")
#--------------------------------------------------------