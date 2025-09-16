from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, "inventory/index.html", {
            "autenticated": request.user.is_authenticated
        })
    else:
        return render(request, "clientside/login.html", {
            "autenticated": request.user.is_authenticated
        })

