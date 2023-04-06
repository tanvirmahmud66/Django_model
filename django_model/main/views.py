from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages
# Create your views here.


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        print(username, email, password, password2)
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "This Email already used")
                redirect('signup')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(
                    user=user_model, userId=user_model.id)
                new_profile.save()
                user = authenticate(username=username, password=password)
                print(user)
                if user is not None:
                    login(request, user)
                    return redirect('profile')
        else:
            messages.error(request, "Password Not Matched")
            redirect('signup')
    return render(request, 'signup.html', {})


def login_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
    return render(request, 'signin.html')


def logout_profile(request):
    logout(request)
    return redirect('signup')


@login_required(login_url='signin')
def profile(request):
    return render(request, 'profile.html')


@login_required(login_url='signin')
def complete_profile(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        profession = request.POST["profession"]
        workplace = request.POST["workplace"]
        user = User.objects.get(username=request.user)
        print(user)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        profile = Profile.objects.get(user=request.user)
        profile.profession = profession
        profile.workplace = workplace
        profile.save()
        return redirect('profile')
    return render(request, 'complete_profile.html')
