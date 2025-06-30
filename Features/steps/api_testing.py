import json
from pathlib import Path
from behave import *

from utils.api_helpers import get_location_from_nominatim
from utils.logger import log

use_step_matcher("re")


@given("user loads lat/lon test data")
def step_load_geo_data(context):
    json_path = Path(__file__).parents[2] / "tests/test_data/apiLocation.json"
    with open(json_path) as f:
        context.geo_data = json.load(f)


@then("each API response should include expected city name")
def step_check_locations(context):
    for entry in context.geo_data:
        lat = entry["latitude"]
        lon = entry["longitude"]
        expected_city = entry["expected_city"].lower()

        url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json"
        context.page.goto(url)

        response_data = get_location_from_nominatim(lat, lon)
        display_name = response_data.get("display_name", "").lower()

        log.info(f"API returned: {display_name}")
        assert expected_city in display_name, f"Expected city '{expected_city}' not found in '{display_name}'"
        log.info(f"Found {expected_city} in response.")
