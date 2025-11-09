import requests
import flight_search
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/4e2ff1e4a3ddfdc4cc8ace67abd75f5d/flightDeals/prices"

class DataManager:

    def __init__(self):
        # Instead of using Basic Authentication, we'll use Bearer Token authentication
        self._bearer_token = os.getenv("SHEETY_TOKEN")  # Make sure to replace with your actual Bearer Token from .env
        self.destination_data = {}

    def get_destination_data(self):
        headers = {
            "Authorization": f"Bearer {self._bearer_token}"
        }

        try:
            response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=headers)
            response.raise_for_status()  # Raise an exception for HTTP errors
            data = response.json()
            self.destination_data = data["prices"]
            return self.destination_data
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None

    def update_destination_codes(self):
        headers = {
            "Authorization": f"Bearer {self._bearer_token}"
        }

        for city in self.destination_data:
            if not city["iataCode"]:  # Check if IATA code is missing
                city["iataCode"] = flight_search.get_destination_code(city["city"])

            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            try:
                response = requests.put(
                    url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                    json=new_data,
                    headers=headers
                )
                response.raise_for_status()  # Raise an exception for HTTP errors
                print(f"Updated IATA code for {city['city']}: {response.text}")
            except requests.exceptions.RequestException as e:
                print(f"Error updating data for {city['city']}: {e}")
