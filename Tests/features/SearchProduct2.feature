Feature: Search Products
  As a user
  I want to search product
  So can check the title of the product related


  Scenario Outline: Check product title
    Given the search is in the header
    When complete "<product>"
    And press the search button
    Then can check the product "<title>"

    Examples: Products Name
    | product | title    |
    | ruby | Ruby Shoo Womens Jada T-Bar |
    | lashes | Lancome Hypnose Doll Lashes Mascara 4-Piece Gift Set |
    | anti-age | Absolute Anti-Age Spot Replenishing Unifying TreatmentSPF 15  |
    | palette | Color Design Eye Brightening All in One 5 Shadow & Liner Palette   |


