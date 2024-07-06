from dotenv import load_dotenv
import os
import requests
import datetime

load_dotenv()
APP_ID = os.getenv('APP_ID')
API_KEY = os.getenv('API_KEY')
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheets_endpoint = f"https://api.sheety.co/{os.getenv('USERNAME')}/workoutTracker/workouts"

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_params = {
    "query": input("What exercises did you perform? \n")
}

exercise_response = requests.post(exercise_endpoint, headers=header, json=exercise_params)
exercise_data = exercise_response.json()["exercises"]

for exercise in exercise_data:
    sheets_params = {
        "workout": {
            "date": datetime.datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.datetime.now().strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    sheets_response = requests.post(sheets_endpoint, json=sheets_params)
    print(sheets_response.text)
