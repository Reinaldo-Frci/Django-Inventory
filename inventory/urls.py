from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<uuid:item_id>", views.item, name="item"),

]