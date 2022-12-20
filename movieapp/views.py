from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieUpdateForm
# Create your views here.


def index(request):
    movies = Movie.objects.all()
    context = {
        'movie_list': movies
    }

    return render(request, 'index.html', context)


def detail_view(request,movie_id):
    movie = Movie.objects.get(id=movie_id)
    context = {
        'movie': movie
    }

    return render(request, 'detail_view.html', context)


def add_movie(request):
    if request.method == 'POST':
        name = request.POST['movie_name']
        banner = request.FILES['movie_banner']
        description = request.POST['movie_des']
        released_year = request.POST['movie_released_year']
        movie = Movie(name=name, banner=banner, description=description, released_year=released_year)
        movie.save()
    return render(request, 'add_movie.html')


def updade_movie_details(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    form = MovieUpdateForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()

        return redirect('/')

    return render(request, 'update_movie.html', {'form': form, 'movie': movie})


def delete_movie_details(request, movie_id):

    if request.method == 'POST':
        movie = Movie.objects.get(id=movie_id)
        movie.delete()
        return redirect('/')

    return render(request, 'delete_movie_details.html')


