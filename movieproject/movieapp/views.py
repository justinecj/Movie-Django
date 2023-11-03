from django.shortcuts import render, redirect
from . models import *
from . forms import  *

# Create your views here.
def movielist(request):
    movies = Movies.objects.all()
    mov = {
        'movies': movies
    }
    return render(request, 'home.html', mov)

def moviedetail(request, movie_id):
    print(movie_id)
    movie = Movies.objects.get(id=movie_id)
    details= {
        'movie':movie
    }
    return render(request,'detail.html', details)

def movieadd(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        data = Movies(name=name, disc=desc, year=year, img=img)
        data.save()
        return redirect('/')
    return render(request,'add.html')

def update(request, id):
    data = Movies.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES, instance=data)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html',{'form':form, 'data':data})

def delete(request, id):
    if request.method == 'POST':
        data = Movies.objects.get(id=id)
        data.delete()
        return redirect('/')
    return render(request, 'delete.html')