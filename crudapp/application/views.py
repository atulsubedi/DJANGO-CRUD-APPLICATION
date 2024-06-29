from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render (request, "index.html")

def insertData(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        print(name, email, age, gender)
    return render(request, "index.html")

    
    
