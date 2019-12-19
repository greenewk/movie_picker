from django.shortcuts import render
from movie_picker.forms import MovieForm
from movie_picker.models import Movie
from django.http import HttpResponseRedirect
from django.urls import reverse

def home(request):
    movies = Movie.objects.all()
    return render(request, 'home.html', {'movies': movies})

def new_movie(request):
    if request == 'POST':
        form = MovieForm(data=request.POST)
        form.save()
        return HttpResponseRedirect(reverse('movie_picker:home'))
    else:
        return HttpResponseRedirect(reverse('movie_picker:home'))
