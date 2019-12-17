from django.test import TestCase
from django.urls import reverse
from selenium import webdriver

class HomePageTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    # Jasper attempts to reach the Super Movie Picker website
    def test_can_reach_homepage(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    # Jasper sees that there is an input box for him to type movies into

    # Jasper types a movie title in and hits Enter

    # The movie title is now in the list!
