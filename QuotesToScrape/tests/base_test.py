from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from unittest import TestCase

class BaseTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://quotes.toscrape.com/")
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    @staticmethod
    def element_locator():
        return {
            "quotes": '//div[@class="quote"]/span[@itemprop="text"]',
            "authors": '//div[@class="quote"]/span/small[@itemprop="author"]',
            "tags": '//div[@class="tags"]/a',
            "next_button": "//li[@class='next']/a",
            "top_tags": "//span[@class='tag-item']/a[@class='tag']",
            "viewing_tag": "//div[@class='container']/h3",
            "about_link": "(//small[@class='author']/following-sibling::a)[1]",
            "about_description": '(//div[@class="author-details"]//child::strong)[2]',
            "login_button": "//p/a[text()='Login']",
            "username_field": "//input[@id='username']",
            "password_field": "//input[@id='password']",
            "submit_button": "//input[@type='submit']",
            "logout_button": "//p/a[@href='/logout']",
            "author_birth_name": "//h3[@class='author-title']",
            "author_birth_date": "//span[@class='author-born-date']",
            "author_birth_location": "//span[@class='author-born-location']",
        }



class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = BaseTest.element_locator()

    def get_quotes(self):
        return [quote.text for quote in self.driver.find_elements(By.XPATH, self.locators["quotes"])]

    def get_authors(self):
        return [author.text for author in self.driver.find_elements(By.XPATH, self.locators["authors"])]

    def click_next_page(self):
        next_btn = self.driver.find_element(By.XPATH, self.locators["next_button"])
        next_btn.click()

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = BaseTest.element_locator()

    def login(self, username, password):
        self.driver.find_element(By.XPATH, self.locators["login_button"]).click()
        self.driver.find_element(By.XPATH, self.locators["username_field"]).send_keys(username)
        self.driver.find_element(By.XPATH, self.locators["password_field"]).send_keys(password)
        self.driver.find_element(By.XPATH, self.locators["submit_button"]).click()

    def is_logged_in(self):
        try:
            self.driver.find_element(By.XPATH, self.locators["logout_button"])
            return True
        except:
            return False

class TestHome(BaseTest):
    def test_quotes_displayed(self):
        home_page = HomePage(self.driver)
        quotes = home_page.get_quotes()
        self.assertGreater(len(quotes), 0, "No quotes found on the homepage")

    def test_authors_displayed(self):
        home_page = HomePage(self.driver)
        authors = home_page.get_authors()
        self.assertGreater(len(authors), 0, "No authors found on the homepage")

    def test_pagination(self):
        home_page = HomePage(self.driver)
        first_page_quotes = home_page.get_quotes()
        home_page.click_next_page()
        second_page_quotes = home_page.get_quotes()
        self.assertNotEqual(first_page_quotes, second_page_quotes, "Pagination not working")

class TestLogin(BaseTest):
    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        login_page.login("admin", "admin")  # Using test credentials
        self.assertTrue(login_page.is_logged_in(), "Login failed with valid credentials")

if __name__ == "__main__":
    unittest.main()
