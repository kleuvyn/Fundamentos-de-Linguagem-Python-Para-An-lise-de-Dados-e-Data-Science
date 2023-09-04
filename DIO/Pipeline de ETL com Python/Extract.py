import pandas as pd

dataframe = pd.read_csv('santander.csv')
user_ids = dataframe['UserID'].tolist()
print(user_ids )

# ----------------------------------------------

import requests
import json

santander_api_url = 'https://sdw-2023-prd.up.railway.app'

def get_user(id):
    response = requests.get(f'{santander_api_url}/users/{id}')
    return response.json() if response.status_code == 200 else None

users = [user for id in user_ids if (user := get_user(id)) is not None]

print(json.dumps(users, indent=2))

