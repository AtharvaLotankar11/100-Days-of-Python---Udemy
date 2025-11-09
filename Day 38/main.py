import requests
from datetime import datetime

# Your personal data. Used by Nutritionix to calculate calories.
GENDER = "male"
WEIGHT_KG = 56
HEIGHT_CM = 170
AGE = 20

# Nutritionix APP ID and API Key. Actual values are stored as environment variables.
APP_ID = "b1a363d8"
API_KEY = "6cc11778ceacc3ef081875d8a82b6e56"
SHETTY_TOKEN = "@fL0cc!n@uC!n!h1l!p!l!f1c@t!0n"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

# Nutritionix API Call
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(f"Nutritionix API call: \n {result} \n")

# Adding date and time
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Sheety Project API. Check your Google sheet name and Sheety endpoint
sheet_endpoint = "https://api.sheety.co/4e2ff1e4a3ddfdc4cc8ace67abd75f5d/myWorkouts/workouts"

# Sheety API Call & Authentication
for exercise in result["exercises"]:
    # Corrected sheet_inputs structure with 'workout' as root key
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # Sheety Authentication Option 3: Bearer Token
    bearer_headers = {
        "Authorization": f"Bearer {SHETTY_TOKEN}"
    }

    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )

    print(f"Sheety Response: \n {sheet_response.text}")
