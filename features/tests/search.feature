# Created by habeeb at 7/5/2025
Feature: Tests for Target Search and Cart Msg

  #Scenario: User can search for tea
   # Given Open target main page
    #When Search for tea
    #Then Verify search worked for tea

#  Scenario: User can search for a mug on Target
#    Given Open target main page
#    When Search for mug
#    Then Verify search worked for mug
#
#  Scenario: User can search for a coffee on Target
#    Given Open target main page
#    When Search for coffee
#    Then Verify search worked for coffee

 #Scenario Outline: User can search for a product
   #Given Open target main page
   #When Search for <search_word>
   #Then Verify search worked for <search_word>
   #Examples:
   #|search_word  |
   #|tea          |
   #|mug          |
   #|coffee       |

 #Scenario: Verify that user can see product names and images
 #  Given Open target main page
  # When Search for AirPods
  # Then Verify that every product has a name and an image


 Scenario: Users can see empty cart message
    Given Open target cart
    When  Click on cart icon
    Then Verify empty cart
    Then Verify Cart page opened

   Scenario: User can access Sign in form
    Given Open Target main page
    When Click on Sign in
    And Click Sign in on side menu
    Then Verify Sign in form opens



    Scenario: User can add a product to cart
    Given Open Target main page
    When Search for mug
    And Click on Add to Cart
    And Confirm Add to Cart button from side navigation
    And Open cart page
    Then Verify cart has 1 item(s)
