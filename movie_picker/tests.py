from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    def get_item_input_box(self):
        return self.browser.find_element_by_name('movie_title')


class HomePageTest(FunctionalTest):

    # Jasper attempts to reach the Super Movie Picker website
    def test_can_reach_homepage(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    # Jasper sees that there is an input box for him to type movies into
    # and it is nicely centered
    def test_movie_title_input_box_present(self):
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )


    # Jasper types a movie title in and hits Enter

    # The movie title is now in the list!
