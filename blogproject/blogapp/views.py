from django.shortcuts import render, redirect
from .models import Post

# Create your views here.


def index(request):
    posts = Post.objects.all()
    return render(
        request,
        "index.html",
        {"posts": posts},
    )


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def getPost(request, postId):
    post = Post.objects.get(id=postId)
    return render(request, "post.html", {"post": post})


# def about(request) => 'about.html'
# def contact(request) => 'contact.html'

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Hi {username}, your account is created successfully!"
            )
            return redirect("blogapp:index")
    else:
        form = UserRegisterForm()
        messages.error(
            request,
            "Sorry, there're something wrong with the system.\nPlease try again in a few seconds.",
        )
    return render(request, "register.html", {"form": form})
