Feature: Displaying Quotes and Authors

  Scenario: Displaying Quotes
    Given the user is on the quotes page
    When the user views the page
    Then the quotes should be displayed

  Scenario: Displaying Authors
    Given the user is on the quotes page
    When the user views the page
    Then the authors should be displayed

  Scenario: Displaying Tags
    Given the user is on the quotes page
    When the user views the page
    Then the tags should be displayed

  Scenario: Navigating Top Tags
    Given the user is on the quotes page
    When the user clicks on a top tag
    Then the tag's page should be displayed

  Scenario: Checking top ten tags
    Given the user is on the quotes page
    When the user views the top tags
    Then there should be no more than ten top tags
