import requests


def get_location_from_nominatim(lat, lon):
    url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json"
    headers = {
        "User-Agent": "eCommCart_QA_Capstone/1.0"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()
