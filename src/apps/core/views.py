from django.shortcuts import render, redirect
from apps.users.forms import  CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from apps.uploader.models import OriginalImage
import  logging 

log = logging.getLogger()
# Create your views here.

def home(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
        image_data=OriginalImage.objects.all()

    return render(request, "home.html", context= {"form": form, "image_data": image_data })


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect('postimage')
        messages.error(request, "Bad Request")
        print(form.errors)
        log.info(form.errors)
    else:
        form = CustomUserCreationForm()

    return render(request, "register.html", context= {"form": form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")
