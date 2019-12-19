from django.shortcuts import render
from movie_picker.forms import MovieForm
from movie_picker.models import Movie

def home(request):
    if request == 'POST':
        form = MovieForm(data=request.POST)
        form.save()
        movies = Movie.objects.all()
        return render(request, 'home.html', {'movies': movies})
    else:
        movies = Movie.objects.all()
        return render(request, 'home.html', {'movies': movies})