from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator import Locators


class QuoteBlocks:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def get_quotes(self):
        return self.wait.until(EC.presence_of_all_elements_located(Locators.QUOTE_TEXT))

    def get_authors(self):
        return self.wait.until(EC.presence_of_all_elements_located(Locators.AUTHOR))

    def get_about_link(self):
        return self.wait.until(EC.presence_of_element_located(Locators.ABOUT_LINK))

    def get_tags(self):
        return self.wait.until(EC.presence_of_all_elements_located(Locators.TAGS))

    def get_top_ten_tags(self):
        return self.wait.until(EC.presence_of_all_elements_located(Locators.TOP_TAGS))

    def get_viewing_tag(self):
        return self.wait.until(EC.presence_of_element_located(Locators.VIEWING_TAG))

    def get_next_btn(self):
        return self.wait.until(EC.presence_of_element_located(Locators.NEXT_BUTTON))

    def click_next_btn(self):
        return self.wait.until(
            EC.presence_of_element_located(Locators.NEXT_BUTTON)
        ).click()

    def get_author_description(self):
        return self.wait.until(
            EC.presence_of_element_located(Locators.ABOUT_DESCRIPTION)
        )