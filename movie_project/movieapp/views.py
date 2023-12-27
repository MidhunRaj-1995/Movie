from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import movie
from .forms import  movie_form

# Create your views here.

def index(request):
    mv = movie.objects.all()
    print(mv)
    context = {"movie_list":mv}
    return render(request,"index.html",context)

def details(request,movie_id):
    mv = movie.objects.get(id = movie_id)
    return render(request,"details.html",{"mv_name":mv})

def add_movie(request):
    if(request.method =='POST'):
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year= request.POST.get('year')
        img = request.FILES['img']
        mv = movie(name=name,desc=desc,year=year,img=img)
        mv.save()
    return render(request,"add_movie.html")

def update(request,id):
    Movie = movie.objects.get(id=id)
    form = movie_form(request.POST or None,request.FILES,instance=Movie)

    if(form.is_valid()):
        form.save()
        return redirect('/')
    return render(request,"edit.html",{"form":form,"movie":Movie})

def delete(request,id):
    if request.method=="POST":
        mv = movie.objects.get(id=id)
        mv.delete()
        return redirect('/')
    return render(request,"delete.html")




