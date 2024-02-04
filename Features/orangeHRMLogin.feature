Feature: OrangeHRM Logo
  Scenario: Login to orangehrm with valid parameters
    Given I launch chrome browser
    When I open orangehrm homepage
    And Enter username "admin" and password "admin123"
    And click on login button
    Then User must successfully login to the dashboard page