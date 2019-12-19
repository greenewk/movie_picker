from django.test import TestCase
from movie_picker.models import Movie
from movie_picker.forms import MovieForm

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

class NewMovieTest(TestCase):

    def test_can_reach_new_movie_page(self):
        response = self.client.post(
            'new_movie', data={'title': 'test'}
        )
        self.assertEqual(response.status_code, 200)

    def test_can_save_POST_request(self):
        self.client.post(
            '/new_movie/', data={'title': 'Terminator 2'}

        )


        self.assertEqual(Movie.objects.count(), 1)
        self.assertEqual(Movie.objects.first().title, 'Terminator 2')



