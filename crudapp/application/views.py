from django.shortcuts import render, redirect
from .models import StudentDB
# Create your views here.

def index(request):
    data=StudentDB.objects.all()
    ctxt = {"data":data}
    return render (request, "index.html", ctxt)

def insertData(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        print(name, email, age, gender)
        query = StudentDB(name=name, email=email, age=age, gender=gender)
        query.save()
        return redirect("/")
    return render(request, "index.html")


def updateData(request, id):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        age=request.POST['age']
        gender=request.POST['gender']

        edit=StudentDB.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.age=age
        edit.gender=gender
        edit.save()
        return redirect("/")
    d=StudentDB.objects.get(id=id)
    ctxt = {"d":d}
    return render (request, "edit.html", ctxt)
    

def deleteData(request, id):
    data=StudentDB.objects.get(id=id)
    data.delete()
    return redirect("/")
