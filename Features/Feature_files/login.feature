Feature: User login

  @login
  Scenario Outline: User logs in with valid credentials
    Given the user navigates to login page
    When the user enters username <username> and password
    Then the user should see the products page
    Examples:
      | username      |
      | standard_user |
      |problem_user   |
