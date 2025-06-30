Feature: Add to Cart

  @sorting
  Scenario Outline: User sorts the products by price Low to High and adds the cheapest item
    Given user has logged in and is now on products page
    When user sorts the products by <option>
    Then user validates the order
    Examples:
      | option              |
      | Price (low to high) |
      | Price (high to low) |

  @AddToCart
  Scenario Outline: Adding an item to the cart
    Given user has logged in and is now on products page
    When the user adds an <item> in the cart
    Then cart badge should contain the expected count
    Examples:
      | item                |
      | Sauce Labs Backpack |

  @RemoveItem
  Scenario: User removes an item from the cart
    Given user has logged in and is now on products page
    And user navigates to the cart
    When user removes an item from cart
    Then the cart badge should not be visible





