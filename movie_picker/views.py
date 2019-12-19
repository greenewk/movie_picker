from django.shortcuts import render
from movie_picker.forms import MovieForm
from movie_picker.models import Movie
from django.http import HttpResponseRedirect
from django.urls import reverse

def home(request):
    movies = Movie.objects.all()
    return render(request, 'home.html', {'movies': movies, 'form': MovieForm()})

def new_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            new_movie = form.save()
            new_movie.save()

        return HttpResponseRedirect(reverse('movie_picker:home'))
    else:
        return HttpResponseRedirect(reverse('movie_picker:home'))
