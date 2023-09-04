import pandas as pd
import requests
import openai

santander_api_url = 'https://sdw-2023-prd.up.railway.app'
dataframe = pd.read_csv('santander.csv')
user_ids = dataframe['UserID'].tolist()

openai_api_key ='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'
openai.api_key = openai_api_key

def get_user(id):
    response = requests.get(f'{santander_api_url}/users/{id}')
    return response.json() if response.status_code == 200 else None

users = [user for id in user_ids if (user := get_user(id)) is not None]


def generate_ai_news(user):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system", ""
                "content": "Oi, você é um especialista em markting comercial ."
            },

            {
                "role": "user",
                "content": f"Crie uma mensagem para {user['name']} sobre a importância  do markting digital (máxomo de 200 caracteres)"
            }
        ]
    )
    return completion.choices[0].message.content.strip('\"')

for user in users:
    news = generate_ai_news(user)
    print(news)
    user[news].append({
        "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
        "description": news
    })