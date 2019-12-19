from movie_picker.forms import MovieForm
from movie_picker.models import Movie
from django.test import TestCase

class MovieFormTest(TestCase):

    def test_form_renders_default_text(self):
        form = MovieForm()
        self.assertIn('placeholder="Enter a movie title"', form.as_p())
