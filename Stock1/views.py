from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout
from .forms import FormLogin  
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def home(request):
   return  render(request, "first.html")

@login_required
def bonne_de_sortie(request):
    if request.method == "POST":
        print(request.POST)
        designation =request.POST.get("designation")
        reference=request.POST.get("reference")
        serial=request.POST.get("serial")
        destination=request.POST.get("destination")
        print(designation)
    return render(request, "bonne_de_sortie/index.html")

@login_required
def loginView(request):
    form = FormLogin() 
    if request.user :
        return redirect("home")
    if request.method == "POST":
        form = FormLogin(data=request.POST)
        if form.is_valid(): 
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password) 
            
            print(user)
            if user is not None:
                login(request, user)  
                return redirect("home")  
    
    context = {"form": form}
    return render(request, "auth/login.html", context)


def logoutView(request):
    logout(request)  
    return redirect("login")  



# crud product
def create(request):
    return render(request,"")
    
 