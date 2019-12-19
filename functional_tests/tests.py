from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import time

MAX_WAIT = 10


class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def get_item_input_box(self):
        return self.browser.find_element_by_id('id_title')

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = (self.browser.find_element_by_id('id_list_table'))
                rows = (table.find_elements_by_tag_name('tr'))
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def wait_for(self, fn):
        start_time = time.time()
        while True:
            try:
                return fn()
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)


class HomePageTest(FunctionalTest):

    # Jasper attempts to reach the Super Movie Picker website
    def test_can_reach_homepage(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    # Jasper types a movie title in and hits Enter
    # The movie title is then in the list
    def test_can_add_movie_to_list(self):
        self.browser.get(self.live_server_url)
        inputbox = self.get_item_input_box()

        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a movie title'
        )


        inputbox.send_keys('Predator')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Predator')

    # Jasper tries to add a movie that is already on his list,
    # but is unable to and is warned of this by an error message

    # Jasper decides that he wants to remove a movie from his list

    # Jasper clicks the "pick a movie" button and is recommended a movie
    # from his list to watch.


