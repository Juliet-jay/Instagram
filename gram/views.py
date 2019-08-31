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
from annoying.decorators import ajax_request
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required


# Create your views here.
