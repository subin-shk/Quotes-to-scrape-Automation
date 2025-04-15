# fixtures.py
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.quotes_page import QuoteBlocks


class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n[Fixture] Setting up class resources")
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.maximize_window()
        cls.wait = WebDriverWait(cls.driver, 5)
        cls.driver.get("https://quotes.toscrape.com/")
        cls.login_page = LoginPage(cls.driver)
        cls.quotes_page = QuoteBlocks(cls.driver)

    @classmethod
    def tearDownClass(cls):
        print("\n[Fixture] Tearing down class resources")
        cls.driver.quit()
