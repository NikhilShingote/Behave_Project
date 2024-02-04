Feature: OrangeHRM Login

# Steps in the Background will be executed before every scenario
# They are common steps in every scenario which you want to execute multiple times
  Background: All The Common Steps
    Given I Launch the CR browser
    When I Open Application
    And I Enter Valid Username and Password
    And I Click on Login Button

  Scenario: Login to HRM Application
    Then  User Must Login to Dashboard Page

  Scenario: Search User
    When Navigate to search Page
    Then Search Page Should Display

  Scenario: Advanced User Search
    When Navigate to Advance Search Page
    Then Advanced Search Page Should Display