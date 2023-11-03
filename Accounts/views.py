from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def register_page(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect("/")
    else: 
        form = UserCreationForm()
    return render(request, "accounts/register.html", {'form': form})


def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponseRedirect("/")
    else:
        form = AuthenticationForm()
        return render(request, "accounts/login.html", {'form': form})


def logout_page(request):
    if request.method == "POST":
        logout(request)
        return HttpResponseRedirect("/")

def profile(request):
    return render(request,'profile.html')