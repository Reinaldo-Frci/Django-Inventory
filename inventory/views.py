from csv import excel

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from idna.idnadata import joining_types
from itertools import chain

from inventory.models import Equipamento, Cabo


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        items = list(Equipamento.objects.all()) + list(Cabo.objects.all())
        return render(request, "inventory/index.html", {
            "autenticated": request.user.is_authenticated,
            "items": items,
        })
    else:
        return render(request, "clientside/login.html", {
            "autenticated": request.user.is_authenticated
        })

def item(request, item_id):
    try:
        item = Equipamento.objects.all().get(pk=item_id)
    except:
        try:
            item = Cabo.objects.all().get(pk=item_id)
        except:
            return HttpResponseRedirect(reverse("inventory:index"))

    if request.user.is_authenticated:
        return render(request, "inventory/item.html", {
            "autenticated": request.user.is_authenticated,
            "item": item,
        })
    else:
        return render(request, "clientside/login.html", {
            "autenticated": request.user.is_authenticated
        })

