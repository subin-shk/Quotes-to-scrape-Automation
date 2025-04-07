import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage

# Load feature scenarios
scenarios("../features/login.feature")


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@given("the user is on the login page")
def open_login_page(driver):
    driver.get("https://quotes.toscrape.com/login")


@when(
    parsers.re(r'the user logs in with username "(.*)" and password "(.*)"')
)
def user_logs_in(login_page, username, password):
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login_button()


@then("the user should be redirected to the home page")
def check_login_success(driver):
    assert (
        driver.current_url != "https://quotes.toscrape.com/login"
    ), "Failed: User was not able to log in"


@then("the user should remain on the login page")
def check_login_fail(driver):
    assert (
        driver.current_url == "https://quotes.toscrape.com/login"
    ), "Failed: User was able to log in with invalid credentials"
3