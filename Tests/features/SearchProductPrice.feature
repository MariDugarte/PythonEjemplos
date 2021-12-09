Feature: Search Products Price
  As a user
  I want to search product
  So can check the price of the product related


  Scenario Outline: Check product price
    Given the search is in the header
    When complete "<product>"
    And press the search button
    Then can check the product "<price>"

    Examples: Products Name
    | product | price |
    | ruby | $78.00 |
    | lashes | $125.00 |
    | anti-age | $42.00 |
    | palette | $48.00 |


