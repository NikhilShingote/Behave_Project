Feature: OrangeHRM Logo

  Scenario Outline: Login with Multiple Parameters
    Given I launch the chrome browser
    When I open orangeHRM page
    And Enter username "<username>" and password "<password>"
    And click the Login button
    Then User must successfully login and go to Dashboard page

    Examples:
      | username | password |
      | admina   | admin123 |
      | admin123 | admin    |
      | Admin    | admin123 |
      | adin     | adminxyz |
