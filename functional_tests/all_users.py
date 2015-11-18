from selenium import webdriver
import unittest
from django.contrib.staticfiles.testing import LiveServerTestCase

# Using unittest testing framework to run tests


class NewUserTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_title_appeare(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Hello', self.browser.title)
if __name__ == '__main__':  #7
    unittest.main(warnings='ignore')