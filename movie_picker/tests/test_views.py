from django.test import TestCase
from movie_picker.models import Movie
from movie_picker.forms import MovieForm

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_uses_movie_form(self):
        response = self.client.get('/')
        self.assertIsInstance(response.context['form'], MovieForm)

    def test_can_save_POST_request(self):
        self.client.post(
            '/', data={'title': 'Terminator 2'}
        )

        self.assertEqual(Movie.objects.count(), 1)
        new_movie = Movie.objects.first()
        self.assertEqual(new_movie.title, 'Terminator 2')