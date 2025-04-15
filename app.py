#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# In[2]:


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# In[3]:


from unittest import TestCase


# In[ ]:


def setup():
    driver = webdriver.Chrome()
    driver.get("https://quotes.toscrape.com/")
    return driver

def teardown(driver):
    driver.quit()


# In[ ]:


# This assertion verifies if the object is an instance of the second parameter class.

class CheckIsInstance(TestCase):
  def check_instance(self):
    driver=setup()
    try:
      self.assertIsInstance (driver, webdriver.Chrome, " Failed: Webdriver is not instance of driver")
      print("Pass: Webdriver is instance of driver")
    except AssertionError as e:
      print(e)
    teardown(driver)
CheckIsInstance().check_instance()


# In[33]:


class TestPageTitle(TestCase):
  def title(self):
    driver=setup()
    try:
      self.assertEqual(driver.title,"Quotes to Scrape", "Failed: Title do not match")
      print("Pass: Website title is correct")
    except AssertionError as e:
      print(e)
    finally:
      teardown(driver)

TestPageTitle().title()


# In[6]:


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
        "author_birth_location": "//span[@class='author-born-location']"
      }


# In[7]:


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


# In[8]:


class AuthorTest(TestCase):
  def get_authors(self):
    driver = setup()
    locators = element_locator()
    authors = driver.find_elements(By.XPATH, locators["authors"])
    try:
      self.assertGreater(len(authors),0, "Failed: No author present")
      
      # assert len(authors) > 0, "No authors found"
      print("Pass: No. of authors: ", len(authors))
    except AssertionError as e:
      print(e)
    for author in authors:
      print(author.text)
    teardown(driver)

test=AuthorTest()
test.get_authors()


# In[83]:


class TagTest(TestCase):
    def get_tags(self):
        driver = setup()
        locators = element_locator()
        tags = driver.find_elements(By.XPATH, locators["tags"])
        try:
            self.assertGreater(len(tags),0, "Failed: Quotes do not have tags")
            # assert len(tags) > 0, "No tags found"
            print("Pass: No. of tags are ", len(tags))
        except AssertionError as e:
            print(e)
        for t in tags:
            print(t.text)
        teardown(driver)
TagTest().get_tags()


# In[ ]:


class TestTopTags(TestCase):
    def top_tags(self):
        driver = setup()
        wait = WebDriverWait(driver, 60)
        locator = element_locator()

        tags = driver.find_elements(By.XPATH, locator['top_tags'])
        
        for tag in tags:
            # tag_text = tag.text
            tag.click()  
            
            viewing_tag = wait.until(
                EC.visibility_of_element_located((By.XPATH, locator['viewing_tag']))
            )
            
            try:
                self.assertIn("Viewing tag", viewing_tag.text, f"Failed: Expected 'Viewing tag' in '{viewing_tag.text}'")
                
                
            except AssertionError as e:
                print(f"Assertion Error: {e}")
            
            driver.back()
            wait.until(EC.presence_of_element_located((By.XPATH, locator['top_tags'])))
        print(f"Pass: Sucessfully navigated into top {len(tags)} tags")
        teardown(driver)

test=TestTopTags()
test.top_tags()


# In[28]:


class TopTenHaveLifeTag(TestCase):
  def havlife(self):
      driver = setup()
      wait = WebDriverWait(driver, 60)
      locator = element_locator()

      tags = driver.find_elements(By.XPATH, locator['top_tags'])
      tag_texts = [tag.text for tag in tags]
      try:
          self.assertIn("life",tag_texts,"Failed: Life tag was not found in top tags")
          print("Pass: Life tag was found in top tags")

          
      except AssertionError as e:
          print(e)

      teardown(driver)

TopTenHaveLifeTag().havlife()


# In[21]:


class LessThanEqualTenTopTags(TestCase):
  def less_equal_ten(self):
    driver=setup()
    locator=element_locator()
    tags = driver.find_elements(By.XPATH, locator['top_tags'])
    try:
      self.assertLessEqual(len(tags),10,"Failed: Top ten tags have more than 10 tags")
      print("Pass: Top ten have no more than 10 tags")
    except AssertionError as e:
      print(e)

    teardown(driver)

LessThanEqualTenTopTags().less_equal_ten()


# In[ ]:





# In[68]:


def top_tags():
    driver = setup()
    wait = WebDriverWait(driver, 60)
    locator = element_locator()

    tags = driver.find_elements(By.XPATH, locator['top_tags'])
    
    for tag in tags:
        tag_text = tag.text
        tag.click()  
        
        viewing_tag = wait.until(
            EC.visibility_of_element_located((By.XPATH, locator['viewing_tag']))
        )
        
        try:
            actualResult = viewing_tag.text 
            assert "Viewing tag" in actualResult, f"Failed: Expected 'Viewing tag' in '{actualResult}'"
            print(f"Successfully navigated inside '{tag_text}' tag!")
            
        except AssertionError as e:
            print(f"Assertion Error: {e}")
        
        driver.back()
        wait.until(EC.presence_of_element_located((By.XPATH, locator['top_tags'])))
    teardown(driver)

top_tags()


# In[31]:


class AuthorDescription(TestCase):
    def check_description(self):
        driver = setup()
        locator=element_locator()
        try:
            about_author= driver.find_element(By.XPATH, locator["about_link"])
            about_author.click()
            expected_result= "Description"
            actual_result = driver.find_element(By.XPATH, "//div[@class='author-details']")
            self.assertIn(expected_result,actual_result.text,"Failed: Author description not found in Author about page.")
            print("Pass: About page contains author description")
        except AssertionError as e:
              print(e)
        finally:
            teardown(driver)
AuthorDescription().check_description()


# In[26]:


class TestTotalQuotes(TestCase):
  def total_quotes(self):
      driver = setup()
      locator=element_locator()
      totalQuotes = 0

      try:
          while True: 
              noOfQuotesPerPage = len(driver.find_elements(By.XPATH, locator['quotes']))
              totalQuotes += noOfQuotesPerPage

              
              next_buttons = driver.find_elements(By.XPATH, locator['next_button'])
              if next_buttons:
                  next_buttons[0].click()  
              else:
                  break 

          self.assertGreater(totalQuotes,50, "Failed: All quotes are not there")
        
          print("Pass: Total no. of quotes: ", totalQuotes)
      except Exception as e:
          print(f"Error: {e}")
      finally:
          teardown(driver)

TestTotalQuotes().total_quotes()


# In[27]:


class  Login(TestCase):
    def login(self):
        driver = setup()
        wait=WebDriverWait(driver,10)
        LoginBtn = driver.find_element(By.XPATH, '//a[@href="/login"]')
        LoginBtn.click()
        username= wait.until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        username.send_keys("name")
        password= wait.until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        password.send_keys("password123")
        submit = driver.find_element(By.XPATH, "//input[@type='submit']")
        submit.click()
        time.sleep(2)
        expected_result="https://quotes.toscrape.com/login"
        try:
            actual_result = driver.current_url
            self.assertNotEqual(actual_result,expected_result, "Failed: User was not able to login")
            print('Pass: User was abe to login')
        except AssertionError as e:
            print(e)
        finally:
            teardown(driver)
Login().login()


# In[13]:


class  EmptyUsernameLogin(TestCase):
    def login_with_empty_username(self):
        driver = setup()
        wait=WebDriverWait(driver,10)
        LoginBtn = driver.find_element(By.XPATH, '//a[@href="/login"]')
        LoginBtn.click()
        username= wait.until(
            EC.presence_of_element_located((By.ID, "username"))
            )
        username.send_keys("")
        password= wait.until(
            EC.presence_of_element_located((By.ID, "password"))
            )
        password.send_keys("password123")
        submit = driver.find_element(By.XPATH, "//input[@type='submit']")
        submit.click()
        time.sleep(2)
        expected_result="https://quotes.toscrape.com/login"
        try:
            actual_result = driver.current_url
            self.assertEqual(actual_result,expected_result, "Failed: User was able to login with empty username")
            print('Pass: User was not abe to login with empty username')
        except AssertionError as e:
            print(e)
        finally:
            teardown(driver)
EmptyUsernameLogin().login_with_empty_username()


# In[12]:


class EmptyPassword(TestCase):
    def login_with_empty_password(self):
        driver = setup()
        wait=WebDriverWait(driver,10)
        LoginBtn = driver.find_element(By.XPATH, '//a[@href="/login"]')
        LoginBtn.click()
        username= wait.until(
            EC.presence_of_element_located((By.ID, "username"))
            )
        username.send_keys("username")
        password= wait.until(
            EC.presence_of_element_located((By.ID, "password"))
            )
        password.send_keys("")
        submit = driver.find_element(
            By.XPATH, "//input[@type='submit']"
            )
        submit.click()
        time.sleep(2)
        expected_result="https://quotes.toscrape.com/login"
        try:
            actual_result = driver.current_url
            self.assertEqual(actual_result,expected_result, 'Failed: User was able to login with empty password')
           
        except AssertionError as e:
            print(e)
        finally:
            teardown(driver)
EmptyPassword().login_with_empty_password()


# In[ ]:


def author_birth():
  driver=setup()
  try:
    i=1
    while i<5:
      about = driver.find_element(By.XPATH, f"(//small[@class='author']/following-sibling::a)[{i}]")
      about.click()
      
      title=driver.find_element(By.XPATH,"//h3[@class='author-title']")
      dob=driver.find_element(By.XPATH,"//span[@class='author-born-date']")
      place=driver.find_element(By.XPATH,"//span[@class='author-born-location']")
      
      print("Name:",title.text)
      print("Date of Birth:",dob.text)
      print("Born",place.text)
      print("-----------------")
      driver.back()
      i += 1
    
  except Exception as e:
    print(e)
author_birth()


# In[88]:


def scroll_slowly():
  driver=setup()
  height = driver.execute_script("return document.body.scrollHeight")
  for scroll in range(100,height,100):
      driver.execute_script(f"window.scrollTo(0,{scroll})")
      time.sleep(0.1)
scroll_slowly()


# In[ ]:


# getting elements one by one
class GetQuotesAuthorTag(TestCase):
    def display(self):
        driver = setup()
        
        quotes = driver.find_elements(By.CLASS_NAME, 'text')  
        authors = driver.find_elements(By.CLASS_NAME, 'author')  
        tags_list = driver.find_elements(By.CLASS_NAME, 'tags')  

        try:
            self.assertGreater(len(quotes),5,"Failed: Couldn't get quotes, authors and tags")
            print("Pass: Was able to retrive quotes, author and tags")
        except AssertionError as e:
            print(e)

        print("-------------------------")

        
        for i in range(len(quotes)):  
            print(f'"{quotes[i].text}"')
            print(f" - by {authors[i].text}")

            tags = tags_list[i].find_elements(By.TAG_NAME, 'a')
    
            
            print("Tags:", " ".join(tag.text for tag in tags))

            
            print()
            print("-------------------------")


        teardown(driver)
    

GetQuotesAuthorTag().display()


# In[ ]:





# In[ ]:


# only first tag
class DisplayFirstTag(TestCase):
    def display_first_tag(self):
        driver = setup()
        
        quotes = driver.find_elements(By.CLASS_NAME, 'text')  
        # authors = driver.find_elements(By.CLASS_NAME, 'author')  
        tags_list = driver.find_elements(By.CLASS_NAME, 'tags')  

        print("-------------------------")

        
        for i in range(len(quotes)):  
            # print(f'"{quotes[i].text}"')
            # print(f" - by {authors[i].text}")

            tags = tags_list[i].find_elements(By.TAG_NAME, 'a')
            tag_texts = [tag.text for tag in tags]
            tag_first=tag_texts[0]

            try:
                self.assertGreater(len(tags),0, "Failed: No tags present")
            except AssertionError as e:
                print(e)

            if tag_texts:
                print(tag_first)

            else:
                print("Tags: None")

            print("-------------------------")
        
        teardown(driver)
DisplayFirstTag().display_first_tag()


# In[ ]:


# same thing but getting elements one by one
# def all_page():
#     driver = setup()
         
#     page=1
#     try:
#         while (page<11):
  
#             quotes=driver.find_elements(By.CSS_SELECTOR, "div[class='quote']")
            
#             for i in range(len(quotes)):
#                 for quote in quotes:
#                     print(quote.text)
#                     print("------------------------")
            
#             if (page==10):
#                 break;
#             else:
#                 nextBtn = driver.find_element(By.CSS_SELECTOR,"li.next")
#                 nextBtn.click()
#     except Exception as e:
#         print(e)
#     finally:
#         teardown(driver)
        

# all_page()

