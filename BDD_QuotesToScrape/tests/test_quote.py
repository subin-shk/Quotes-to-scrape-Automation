import pytest
from pytest_bdd import scenarios, given, when, then
from pages.quotes_page import QuoteBlocks

scenarios("../features/quote.feature")


@pytest.fixture
def quote_page(driver):
    return QuoteBlocks(driver)


@given("the user is on the quotes page")
def open_quotes_page(driver):
    driver.get("https://quotes.toscrape.com")


@when("the user views the page")
def user_views_page():
    pass  


@when("the user clicks on a top tag")
def user_clicks_top_tag(quote_page):
    top_tags = quote_page.get_top_ten_tags()
    assert top_tags, "No top tags found"
    top_tags[0].click()


@when("the user views the top tags")
def user_views_top_tags():
    pass


@then("the quotes should be displayed")
def quotes_should_be_displayed(quote_page):
    quotes = quote_page.get_quotes()
    assert len(quotes) > 0, "Failed: No quotes displayed"


@then("the authors should be displayed")
def authors_should_be_displayed(quote_page):
    authors = quote_page.get_authors()
    assert len(authors) > 0, "Failed: No authors displayed"


@then("the tags should be displayed")
def tags_should_be_displayed(quote_page):
    tags = quote_page.get_tags()
    assert len(tags) > 0, "Failed: No tags displayed"


@then("the tag's page should be displayed")
def tag_page_should_display(quote_page):
    viewing_tag = quote_page.get_viewing_tag()
    assert (
        "Viewing tag" in viewing_tag.text
    ), f"Failed: Expected 'Viewing tag' in '{viewing_tag.text}'"


@then("there should be no more than ten top tags")
def top_tags_limit(quote_page):
    tags = quote_page.get_top_ten_tags()
    assert len(tags) <= 10, "Failed: More than 10 top tags found"
