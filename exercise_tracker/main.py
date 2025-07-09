import requests
from datetime import datetime
import os

APP_ID = "6a085bd2"
APP_KEY = "bff83e67297651002d7bf7ce5c6426da"
GENDER = "male"
WEIGHT_KG = 62
HEIGHT_CM = 170
AGE = 21
USERNAME="inder_kukreja"
PASSWORD="apple@123"
TOKEN="samdam"
SHEETY_ENDPOINT = "https://api.sheety.co/bcf87cd5a8be35808ef11c8080784991/workoutTracking/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

exercise_text = input("Tell me which exercises you did: ")

nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutrition_param = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=nutrition_endpoint, json=nutrition_param, headers=headers)
result = response.json()

date_now = datetime.now().strftime("%d/%m/%Y")
time_now = datetime.now().strftime("%H:%M:%S")

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


bearer_headers = {
"Authorization": f"Bearer {TOKEN}"
}
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(SHEETY_ENDPOINT, json=sheet_inputs,headers=bearer_headers)

    print(sheet_response.text)
