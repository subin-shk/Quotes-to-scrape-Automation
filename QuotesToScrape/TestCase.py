from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from unittest import TestCase
import unittest
from selenium.common.exceptions import TimeoutException
from pages.login_page import LoginPage
from pages.quotes_page import QuoteBlocks
from locator import Locators
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from fixtures import BaseTest
import pytest


class QuotesToScrape(BaseTest):

    def test_title(self):
        title = self.driver.title
        try:
            self.assertEqual(title, "Quotes to Scrape", "Failed: Title do not match")
            print("Pass: Website title is correct")
        except AssertionError as e:
            print(e)

    def test_valid_login(self):
        self.login_page.click_login_btn()
        self.login_page.enter_username("username")
        self.login_page.enter_password("password")
        self.login_page.click_login_button()
        expected_result = "https://quotes.toscrape.com/login"
        # self.driver.implicitly_wait(1)
        try:
            actual_result = self.driver.current_url
            self.assertNotEqual(
                actual_result, expected_result, "Failed: User was not able to login"
            )

            print("Pass: User was able to login")
        except AssertionError as e:
            print(e)

    def test_login_with_empty_username(self):
        self.login_page.click_login_btn()
        self.login_page.enter_username("")
        self.login_page.enter_password("password")
        self.login_page.click_login_button()
        self.driver.implicitly_wait(1)
        expected_result = "https://quotes.toscrape.com/login"
        try:
            actual_result = self.driver.current_url
            self.assertEqual(
                actual_result,
                expected_result,
                "Failed: User was able to login with empty username",
            )
            print("Pass: User was not abe to login with empty username")
        except AssertionError as e:
            print(e)

    def test_login_with_empty_password(self):
        self.login_page.click_login_btn()
        self.login_page.enter_username("username")
        self.login_page.enter_password("")
        self.login_page.click_login_button()
        self.driver.implicitly_wait(1)
        expected_result = "https://quotes.toscrape.com/login"
        try:
            actual_result = self.driver.current_url
            self.assertEqual(
                actual_result,
                expected_result,
                "Failed: User was able to login with empty password",
            )
        except AssertionError as e:
            print(e)

    def test_display_quotes(self):
        quotes = self.quotes_page.get_quotes()
        try:
            self.assertGreater(len(quotes), 0, "Failed: No Quotes displayed")
            # assert len(quotes) > 0, "No quotes found"
            print("Pass: No. of quotes: ", len(quotes))
        except AssertionError as e:
            print(e)
        # for val in quotes:
        #     print(val.text)

    def test_display_authors(self):
        authors = self.quotes_page.get_authors()
        try:
            self.assertGreater(len(authors), 0, "Failed: No author present")

            # assert len(authors) > 0, "No authors found"
            print("Pass: No. of authors: ", len(authors))
        except AssertionError as e:
            print(e)
        # for author in authors:
        #     print(author.text)

    def test_display_tags(self):
        tags = self.quotes_page.get_tags()
        try:
            self.assertGreater(len(tags), 0, "Failed: Quotes do not have tags")
            # assert len(tags) > 0, "No tags found"
            print("Pass: No. of tags are ", len(tags))
        except AssertionError as e:
            print(e)
        # for t in tags:
        #     print(t.text)

    def test_top_tags(self):
        tags = self.quotes_page.get_top_ten_tags()

        for tag in tags:
            # tag_text = tag.text
            tag.click()

            viewing_tag = self.quotes_page.get_viewing_tag()

            try:
                self.assertIn(
                    "Viewing tag",
                    viewing_tag.text,
                    f"Failed: Expected 'Viewing tag' in '{viewing_tag.text}'",
                )

            except AssertionError as e:
                print(f"Assertion Error: {e}")

            self.driver.back()
            # self.quotes_page.get_tags()
        print(f"Pass: Sucessfully navigated into top {len(tags)} tags")

    def test_less_equal_ten_top_tags(self):
        tags = self.quotes_page.get_top_ten_tags()
        try:
            self.assertLessEqual(
                len(tags), 10, "Failed: Top ten tags have more than 10 tags"
            )
            print("Pass: Top ten have no more than 10 tags")
        except AssertionError as e:
            print(e)

    def test_author_description(self):

        try:
            about_author = self.quotes_page.get_about_link()

            about_author.click()

            expected_result = "Description"
            actual_result = self.quotes_page.get_author_description()
            self.assertIn(
                expected_result,
                actual_result.text,
                "Failed: Author description not found in Author about page.",
            )
            print("Pass: About page contains author description")
        except AssertionError as e:
            print(e)

    # def test_10_total_quotes(self):
    #     totalQuotes = 0

    #     try:
    #         while True:
    #             quotes = self.quotes_page.get_quotes()
    #             noOfQuotesPerPage = len(quotes)
    #             totalQuotes += noOfQuotesPerPage

    #             next_buttons = self.quotes_page.get_next_btn()
    #             if next_buttons:
    #                 next_buttons[0].click()
    #             else:
    #                 break

    #         self.assertGreater(totalQuotes, 50, "Failed: All quotes are not there")

    #         print("Pass: Total no. of quotes: ", totalQuotes)
    #     except Exception as e:
    #         print(f"Error: {e}")

    def test_11_display_all(self):

        quotes = self.quotes_page.get_quotes()
        authors = self.quotes_page.get_authors()
        tags_list = self.quotes_page.get_tags()

        try:
            self.assertGreater(
                len(quotes), 5, "Failed: Couldn't get quotes, authors and tags"
            )
            print("Pass: Was able to retrive quotes, author and tags")
        except AssertionError as e:
            print(e)

        # print("-------------------------")

        # for i in range(len(quotes)):
        #     print(f'"{quotes[i].text}"')
        #     print(f" - by {authors[i].text}")

        #     tags = tags_list[i].find_elements(By.TAG_NAME, "a")

        #     print("Tags:", " ".join(tag.text for tag in tags))

        #     print()
        #     print("-------------------------")


if __name__ == "__main__":
    # unittest.main(defaultTest="QuotesToScrape.test_display_all")
    unittest.main()
    # globals()[sys.argv[1]]()
    # test_display_quotes()
