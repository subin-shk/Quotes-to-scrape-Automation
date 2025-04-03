from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator import Locators

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def click_login_btn(self):
        self.wait.until(EC.element_to_be_clickable(Locators.LOGIN)).click()

    def enter_username(self, username):
        self.wait.until(EC.presence_of_element_located(Locators.USERNAME_FIELD)).send_keys(username)

    def enter_password(self, password):
        self.wait.until(EC.presence_of_element_located(Locators.PASSWORD_FIELD)).send_keys(password)

    def click_login_button(self):
        self.wait.until(EC.element_to_be_clickable(Locators.SUBMIT_BUTTON)).click()

    def is_logout_link_visible(self):
        return self.wait.until(EC.presence_of_element_located(Locators.LOGOUT_BUTTON )).text 
    
    # def login_error_msg(self):
    #     return self.wait.until(EC.presence_of_element_located(Locators.LOGIN_ERROR)).text