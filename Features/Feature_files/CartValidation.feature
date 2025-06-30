Feature: To validate the cart

  @CartValidation
  Scenario: User adds products to cart and validates the cart items
    Given user has logged in and is now on products page
    When user adds all items to the cart from json file
    Then the user should see those items in the cart with correct names and prices

