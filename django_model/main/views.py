from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        print(username, email, password, password2)
    return render(request, 'index.html', {})
