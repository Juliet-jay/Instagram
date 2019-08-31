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

@login_required
def update_profile(request, username):
  user = User.objects.get(username = username)
  if request.method == 'POST':
    user_form = UserForm(request.POST, instance = request.user)
    profile_form = ProfileForm(request.POST, instance = request.user.profile,files =request.FILES)
    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile_form.save()
      messages.success(request, ('Your profile was successfully updated!'))
      return redirect(reverse('profile', kwargs={'username': request.user.username}))
    else:
      messages.error(request, ('Please correct the error below.'))
  else:
    user_form = UserForm(instance = request.user)
    profile_form = ProfileForm(instance = request.user.profile)
  return render(request, 'profiles/profile_form.html', {"user_form": user_form,"profile_form": profile_form})

@login_required
def profile(request, username):
  user = User.objects.get(username = username)
  if not user:
    return redirect('Home')
  profile = Profile.objects.get(user =user)


  title = f"{user.username}"
  return render(request, 'profiles/profile.html', {"title": title, "user":user, "profile":profile})

def followers(request, username):
  user = user = User.objects.get(username = username)
  user_profile = Profile.objects.get(user=user)
  profiles = user_profile.followers.all

  title = "Followers"

  return render(request, 'follow_list.html', {"title": title, "profiles":profiles})

def following(request, username):
  user = user = User.objects.get(username = username)
  user_profile = Profile.objects.get(user=user)
  profiles = user_profile.following.all()

  title = "Following"

  return render(request, 'follow_list.html', {"title": title, "profiles":profiles})

def likes(request, pk):
  post = Post.objects.get(pk=pk)
  profiles = Like.objects.filter(post=post)

  title = 'Likes'
  return render(request, 'follow_list.html', {"title": title, "profiles":profiles})

def search(request):        
    if request.method == 'POST':      
        profile =  request.POST.getprofile('search')      
        try:
            status = Add_prod.objects.filter(profile__icontains=profile)
            #Add_prod class contains a column
        except Add_prod.DoesNotExist:
            status = None
        return render(request,"search.html",{"books":status})
    else:
        return render(request,"search.html",{})    








