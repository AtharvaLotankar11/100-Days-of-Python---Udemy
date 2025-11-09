#Rain_Alert Project
import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "YOUR_OPENWEATHERMAP_API_KEY"
account_sid = "YOUR_TWILIO_ACCOUNT_SID"
auth_token = "YOUR_TWILIO_AUTH_TOKEN"

#Knin raining - now
weather_params = {
    "lat": 44.037102,
    "lon": 16.197300,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

for hour_data in weather_data["weather"]:
    condition_code = hour_data["id"]

    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="whatsapp:YOUR_TWILIO_WHATSAPP_NUMBER",
        to="whatsapp:YOUR_PHONE_NUMBER"
    )
    print(message.status)

