Feature: Login and Logout in Store
  As a user
  I want to access and leave the Store page
  So Login and Logout correctly

  Scenario: Login and Logout to the store webPage

    Given the Login Store webPage
    When complete "mariDugarte" and "automation"
    Then my account page is displayed
    Then press the Logout button
    Then can logout me








