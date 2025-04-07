from selenium.webdriver.common.by import By


class Locators:
    QUOTE_TEXT = (By.XPATH, '//div[@class="quote"]/span[@itemprop="text"]')
    AUTHOR = (By.XPATH, '//div[@class="quote"]/span/small[@itemprop="author"]')
    TAGS = (By.XPATH, '//div[@class="tags"]/a')
    NEXT_BUTTON = (By.XPATH, "//li[@class='next']/a")
    TOP_TAGS = (By.XPATH, "//span[@class='tag-item']/a[@class='tag']")
    VIEWING_TAG = (By.XPATH, "//div[@class='container']/h3")
    ABOUT_LINK = (By.XPATH, "(//small[@class='author']/following-sibling::a)[1]")
    ABOUT_DESCRIPTION = (By.XPATH, '(//div[@class="author-details"]//child::strong)[2]')
    LOGIN = (By.XPATH, '//a[@href="/login"]')
    LOGIN_BUTTON = (By.XPATH, "//p/a[text()='Login']")
    USERNAME_FIELD = (By.XPATH, "//input[@id='username']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
    SUBMIT_BUTTON = (By.XPATH, "//input[@type='submit']")
    LOGOUT_BUTTON = (By.XPATH, "//p/a[@href='/logout']")
    AUTHOR_BIRTH_NAME = (By.XPATH, "//h3[@class='author-title']")
    AUTHOR_BIRTH_DATE = (By.XPATH, "//span[@class='author-born-date']")
    AUTHOR_BIRTH_LOCATION = (By.XPATH, "//span[@class='author-born-location']")
