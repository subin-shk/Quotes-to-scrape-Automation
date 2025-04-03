from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from base_test import BaseTest

class QuoteTest(TestCase):
    def get_quotes(self):
        driver = setup()
        locators = element_locator()
        quotes = driver.find_elements(By.XPATH, locators["quotes"])
        try:
            self.assertGreater ( len(quotes), 0, "Failed: No Quotes displayed")
            # assert len(quotes) > 0, "No quotes found"
            print("Pass: No. of quotes: ", len(quotes))
        except AssertionError as e:
            print(e)
        for val in quotes:
            print(val.text)
        teardown(driver)

test = QuoteTest()
test.get_quotes()