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
        firstname = request.POST["first_name"]
        lastname = request.POST["last_name"]
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
                    username=username, email=email, first_name=firstname, last_name=lastname, password=password)
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
        bio = request.POST["bio"]
        profession = request.POST["profession"]
        workplace = request.POST["workplace"]
        gender = request.POST["gender"]
        relation_ship = request.POST["relationStatus"]
        user = User.objects.get(id=request.user.id)
        print(user)
        if not user.is_staff:
            profile = Profile.objects.get(user=request.user)
            profile.bio = bio
            profile.profession = profession
            profile.workplace = workplace
            profile.gender = gender
            profile.relationStatus = relation_ship
            profile.save()
        return redirect('profile')
    return render(request, 'complete_profile.html')


@login_required(login_url='signin')
def edit_profile(request):
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        bio = request.POST["bio"]
        firstname = request.POST["first_name"]
        lastname = request.POST["last_name"]
        email = request.POST["email"]
        profession = request.POST["profession"]
        workplace = request.POST["workplace"]
        gender = request.POST["gender"]
        relation = request.POST["relationStatus"]
        print(bio, firstname, lastname, email,
              profession, workplace, gender, relation)
        user.first_name = firstname
        user.last_name = lastname
        user.email = email
        user.save()
        profile.bio = bio
        profile.profession = profession
        profile.workplace = workplace
        profile.gender = gender
        profile.relationStatus = relation
        profile.save()
        return redirect('profile')
    return render(request, 'edit_profile.html', {
        "user": user,
        "profile": profile,
    })


@login_required(login_url='login')
def create_post(request):
    return render(request, 'create_post.html')
