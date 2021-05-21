from django.shortcuts import render
from django.http import HttpResponse
import random
import string


# Create your views here.


def home(request):
    return render(request, "generator/home.html")


def password(request):
    length = int(request.GET.get("length", 12))

    the_password_characters = string.ascii_lowercase

    if request.GET.get("uppercase"):
        the_password_characters = string.ascii_letters

    if request.GET.get("numbers"):
        the_password_characters += string.digits

    if request.GET.get("special"):
        the_password_characters += string.punctuation

    the_password = "".join(random.choices(the_password_characters, k=length))

    return render(request, "generator/password.html", {"password": the_password})


def about(request):
    return render(request, "generator/about.html")
