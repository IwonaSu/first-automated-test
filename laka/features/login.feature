Feature: As a register user I want to log in into my account.

Scenario: Successful log in.
    Given the page is loaded
    When I click on log in button
    And I fill in username
    And I fill in password
    And I submit the data
    Then I am logged user
