from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/home")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form":form})