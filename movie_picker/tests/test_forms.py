from movie_picker.forms import MovieForm
from movie_picker.models import Movie
from django.test import TestCase

class MovieFormTest(TestCase):

    def test_form_renders_default_text(self):
        form = MovieForm()
        self.assertIn('placeholder="Enter a movie title"', form.as_p())

    def test_form_can_save_movie(self):
        form = MovieForm(data={'title': 'Kindergarten Cop'})
        new_movie = form.save()
        self.assertEqual(new_movie, Movie.objects.first())
        self.assertEqual(new_movie.title, 'Kindergarten Cop')
