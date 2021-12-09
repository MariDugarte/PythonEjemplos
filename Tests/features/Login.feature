Feature: Login in Store
  As a user
  I want to access the Store page
  So Login correctly

  Background:
    Given the Login Store webPage

  Scenario: Login in store webPage
    When complete "mariDugarte" and "automation"
    Then my account page is displayed

  Scenario: Complete user and password wrong
    When complete "aaaaa" and "aaaaa"
    Then the error "Error: Incorrect login or password provided." is displayed

