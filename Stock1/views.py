from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout
from .forms import FormLogin  
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product

def home(request):
    if request.method == "POST":
        designation =request.POST.get("designation")
        reference=request.POST.get("reference")
        serial=request.POST.get("serial")
        destination=request.POST.get("destination")
        product = Product(destignation=designation, referance=reference, serial_number=serial, destination=destination)
        product.save()
    products = Product.objects.all()
    contxet={
        "products": products
    }
    return  render(request, "first.html",context=contxet)

@login_required
def bonne_de_sortie(request):
    if request.method == "POST":
        designation =request.POST.get("designation")
        reference=request.POST.get("reference")
        serial=request.POST.get("serial")
        destination=request.POST.get("destination")
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



 