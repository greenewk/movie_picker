from django.test import TestCase
from movie_picker.models import Movie, User
from django.core.exceptions import ValidationError

class MovieModelTest(TestCase):

    def test_default_title(self):
        movie = Movie()
        self.assertEqual(movie.title, '')

    def test_string_representation(self):
        movie = Movie(title='True Lies')
        self.assertEqual(str(movie), 'True Lies')

    def test_cannot_save_empty_movie(self):
        movie = Movie(title='')
        with self.assertRaises(ValidationError):
            movie.save()
            movie.full_clean()

    def test_movie_has_correct_owner(self):
        bob = User.objects.create_user(username="Bob")
        george = User.objects.create_user(username="George")
        movie = Movie(title='test')
        movie.user = bob
        movie.save()
        self.assertEqual(movie.user, bob)

