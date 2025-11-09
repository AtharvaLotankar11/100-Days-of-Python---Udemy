import os
from pprint import pprint
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class DataManager:

    def __init__(self):
        """
        Initializes the DataManager instance with the Sheety Token.
        """
        self._sheety_token = os.environ["SHEETY_TOKEN"]
        # Save your Sheety endpoints as environment variables
        self.prices_endpoint = os.environ["SHEETY_PRICES_ENDPOINT"]
        self.users_endpoint = os.environ["SHEETY_USERS_ENDPOINT"]
        # Authorization header for requests
        self._headers = {"Authorization": f"Bearer {self._sheety_token}"}
        # Destination and Customer fields data start out empty
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        """
        Get destination data from Sheety using the token-based authentication.
        """
        response = requests.get(url=self.prices_endpoint, headers=self._headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        """
        Update destination codes in Sheety by making a PUT request with IATA codes.
        """
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.prices_endpoint}/{city['id']}",
                json=new_data,
                headers=self._headers
            )
            print(response.text)

    def get_customer_emails(self):
        """
        Get customer emails from Sheety.
        """
        response = requests.get(url=self.users_endpoint, headers=self._headers)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
