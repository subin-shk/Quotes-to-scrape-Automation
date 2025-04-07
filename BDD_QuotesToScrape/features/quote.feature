Feature: Quotes to Scrape Website Testing

  Scenario: Verify website title
    Given the user opens the Quotes website
    Then the title should be "Quotes to Scrape"

  Scenario: User logs in with valid credentials
    Given the user opens the Quotes website
    When the user logs in with username "username" and password "password"
    Then the user should be logged in successfully

  Scenario: User tries to log in with an empty username
    Given the user opens the Quotes website
    When the user logs in with username "" and password "password"
    Then the user should remain on the login page

  Scenario: User tries to log in with an empty password
    Given the user opens the Quotes website
    When the user logs in with username "username" and password ""
    Then the user should remain on the login page

  Scenario: Verify quotes are displayed
    Given the user opens the Quotes website
    Then at least one quote should be displayed

  Scenario: Verify authors are displayed
    Given the user opens the Quotes website
    Then at least one author should be displayed

  Scenario: Verify tags are displayed
    Given the user opens the Quotes website
    Then at least one tag should be displayed

  Scenario: Navigate through top tags
    Given the user opens the Quotes website
    When the user clicks on each top tag
    Then the tag page should display "Viewing tag"

  Scenario: Verify there are at most 10 top tags
    Given the user opens the Quotes website
    Then the number of top tags should not exceed 10

  Scenario: Verify author description page
    Given the user opens the Quotes website
    When the user clicks on an author’s "about" link
    Then the author description should be visible

  Scenario: Verify quotes, authors, and tags are displayed together
    Given the user opens the Quotes website
    Then the page should display quotes, authors, and tags
