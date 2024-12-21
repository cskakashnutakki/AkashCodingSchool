from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def courses(request):
    return render(request, 'courses.html')

def bootcamp(request):
    return render(request, 'bootcamp.html')

def requestcallback(request):
    return render(request, 'requestcallback.html')

def signin(request):
    return render(request, 'signin.html')