# Created by habeeb at 6/28/2025
Feature:Target UI test and add item to cart

  Scenario: Target Circle has correct amount of Benefit Boxes
    Given  open Target Circle page
    Then Verify Circle Benefits are present
    And Verify page has 10 benefits boxes




   Scenario: User can add a product to cart
    Given Open Target main page
    When Search for mug
    And Click on Add to Cart button
    And Confirm Add to Cart button from side navigation
    And Open cart page
    Then Verify cart has 1 item(s)
    And Verify cart has correct product


