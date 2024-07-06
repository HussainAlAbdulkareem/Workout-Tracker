from dotenv import load_dotenv
import os
import requests

load_dotenv()
APP_ID = os.getenv('APP_ID')
API_KEY = os.getenv('API_KEY')
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_params = {
    "query": input("What exercises did you perform? ")
}

response = requests.post(exercise_endpoint, headers=header, json=exercise_params)
print(response.text)
