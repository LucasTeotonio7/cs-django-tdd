from django.test import LiveServerTestCase
from selenium import webdriver

class AnimalsTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('/home/lucas/workspace/cs-django-tdd/chromedriver.exe')


    def tearDown(self):
        self.browser.quit()
