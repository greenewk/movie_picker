from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep

class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    def get_item_input_box(self):
        return self.browser.find_element_by_name('movie_title')

    def check_row_is_in_list_table(self, row_text):
        table = (self.browser.find_element_by_id('id_list_table'))
        rows = (table.find_elements_by_tag_name('tr'))
        self.assertIn(row_text, [row.text for row in rows])
        return

class HomePageTest(FunctionalTest):

    # Jasper attempts to reach the Super Movie Picker website
    def test_can_reach_homepage(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    # Jasper sees that there is an input box for him to type movies into
    # and it is nicely centered


    # Jasper types a movie title in and hits Enter
    # The movie title is then in the list
    def test_can_add_movie_to_list(self):
        self.browser.get(self.live_server_url)
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Predator')
        inputbox.send_keys(Keys.ENTER)
        self.check_row_is_in_list_table('Predator')

