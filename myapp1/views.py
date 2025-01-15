from django.shortcuts import render,redirect

# from .models import courses,callback

from .forms import callbackForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def courses(request):
    return render(request, 'courses.html')

def bootcamp(request):
    return render(request, 'bootcamp.html')

def requestcallback(request):
    if request.method=='POST':
        form=callbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp1:home')    
    return render(request, 'requestcallback.html',{'form':callbackForm()})

def signin(request):
    return render(request, 'signin.html')

# def courses(request,id):
#     return render(request, 'courses.html')