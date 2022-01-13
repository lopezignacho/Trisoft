from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def login(request):
    return render(request, 'app/registro/login.html')

def registro(request):
    return render(request, 'app/registro/registro.html')
