from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import *


# Create your views here.
def homepage(request):
    return render(request, 'Anasayfa.html')


def hakkimizda(request):
    return render(request, 'Hakkimizda.html')


def iletisim(request):
    return render(request, 'Iletisim.html')


def giris(request):
    form = UserLoginForm(request.POST or None)
    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("http://127.0.0.1:8000/Anasayfa")
            else:
                messages.error(request, 'Kullanıcı adı ya da şifre hatalı')
                return redirect("http://127.0.0.1:8000/Giris")
    return render(request, "Giris.html", {'form': form})


@login_required(login_url="http://127.0.0.1:8000/Giris")
def cikis(request):
    logout(request)
    return redirect("http://127.0.0.1:8000/Anasayfa")
