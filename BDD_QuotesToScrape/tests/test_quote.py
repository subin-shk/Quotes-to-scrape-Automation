import pytest
from pytest_bdd import scenarios, given, when, then
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.quotes_page import QuoteBlocks

# from fixtures import BaseTest

# Load feature scenarios
scenarios("../features/quotes.feature")


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def quotes_page(driver):
    return QuoteBlocks(driver)


@given("the user opens the Quotes website")
def open_website(driver):
    driver.get("https://quotes.toscrape.com")


@then('the title should be "Quotes to Scrape"')
def check_title(driver):
    assert driver.title == "Quotes to Scrape", "Failed: Title does not match"


@when('the user logs in with username "<username>" and password "<password>"')
def user_logs_in(login_page, username, password):
    login_page.click_login_btn()
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login_button()


@then("the user should be logged in successfully")
def check_login_success(driver):
    assert (
        driver.current_url != "https://quotes.toscrape.com/login"
    ), "Failed: User was not able to log in"


@then("the user should remain on the login page")
def check_login_fail(driver):
    assert (
        driver.current_url == "https://quotes.toscrape.com/login"
    ), "Failed: User was able to log in with invalid credentials"


@then("at least one quote should be displayed")
def check_quotes_displayed(quotes_page):
    assert len(quotes_page.get_quotes()) > 0, "Failed: No quotes displayed"


@then("at least one author should be displayed")
def check_authors_displayed(quotes_page):
    assert len(quotes_page.get_authors()) > 0, "Failed: No authors displayed"


@then("at least one tag should be displayed")
def check_tags_displayed(quotes_page):
    assert len(quotes_page.get_tags()) > 0, "Failed: No tags displayed"


@when("the user clicks on each top tag")
def click_top_tags(quotes_page):
    for tag in quotes_page.get_top_ten_tags():
        tag.click()


@then('the tag page should display "Viewing tag"')
def check_tag_page(quotes_page):
    viewing_tag = quotes_page.get_viewing_tag()
    assert (
        "Viewing tag" in viewing_tag.text
    ), "Failed: Tag page does not show 'Viewing tag'"


@then("the number of top tags should not exceed 10")
def check_top_tags_count(quotes_page):
    assert (
        len(quotes_page.get_top_ten_tags()) <= 10
    ), "Failed: More than 10 top tags are displayed"


@when('the user clicks on an author’s "about" link')
def click_author_about(quotes_page):
    quotes_page.get_about_link().click()


@then("the author description should be visible")
def check_author_description(quotes_page):
    assert (
        "Description" in quotes_page.get_author_description().text
    ), "Failed: Author description not found"


@then("the page should display quotes, authors, and tags")
def check_display_all(quotes_page):
    assert (
        len(quotes_page.get_quotes()) > 5
    ), "Failed: Couldn't retrieve quotes, authors, and tags"
