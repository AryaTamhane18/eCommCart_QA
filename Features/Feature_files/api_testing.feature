Feature: Verify city name from reverse geolocation API

  @GeoAPI
  Scenario: Check location from coordinates
    Given user loads lat/lon test data
    Then each API response should include expected city name
