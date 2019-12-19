from django.test import TestCase
from movie_picker.models import Movie
from movie_picker.forms import MovieForm
from django.urls import reverse

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get(reverse('movie_picker:home'))
        self.assertTemplateUsed(response, 'home.html')

class NewMovieTest(TestCase):

    def test_NON_POST_requests_redirect_to_home(self):
        response = self.client.get('/movie_picker/new_movie')
        self.assertEqual(response.status_code, 301)

    def test_can_save_POST_request(self):
        self.client.post(
            '/movie_picker/new_movie/', data={'title': 'Terminator 2'}
        )


        self.assertEqual(Movie.objects.count(), 1)
        self.assertEqual(Movie.objects.first().title, 'Terminator 2')



