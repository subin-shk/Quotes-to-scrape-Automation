Feature: User Login Functionality

  Scenario: User logs in with valid credentials
    Given the user is on the login page
    When the user logs in with username "validuser" and password "validpassword"
    Then the user should be redirected to the home page

  Scenario: User tries to log in with an empty username
    Given the user is on the login page
    When the user logs in with username "" and password "validpassword"
    Then the user should remain on the login page

  Scenario: User tries to log in with an empty password
    Given the user is on the login page
    When the user logs in with username "validuser" and password ""
    Then the user should remain on the login page

