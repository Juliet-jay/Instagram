from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.conf import settings
from django.conf.urls import url,include
from django.contrib.auth import authenticate, login, logout
from .forms import PostForm
from django.conf.urls.static import static
from .models import Profile, Image
from django.contrib.auth.models import User
from . import models
# from annoying.decorators import ajax_request
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    all_images = Image.objects.all()
    all_users = Profile.objects.all()
    next = request.GET.get('next')
    if next: return redirect(next)
    return render(request, 'account.html',  {"all_images": all_images}, {"all_users":all_users})

def explore(request):
    return render(request, 'user_list.html')

def profile(request):
    return render(request, 'profile.html')

def logout(request):
    return render(request, 'registration/logout.html')


def login(request):
    return render(request, 'registration/login.html')
    

def upload(request):
    current_user = request.user
    p = Profile.objects.filter(id=current_user.id).first()
    imageuploader_profile = Image.objects.filter(imageuploader_profile=p).all()
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.imageuploader_profile= p
            post.save()
            return redirect('index')
    else:
        form =PostForm
    return render(request, 'post_pic.html', {"form": form})

