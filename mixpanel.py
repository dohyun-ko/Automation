import json

import requests
import dotenv
import os

def get_mixpanel_data():
    """Get data from Mixpanel API"""
    dotenv.load_dotenv()
    username = os.getenv('USERNAME')
    secret = os.getenv('SECRET')
    api_url = 'https://data.mixpanel.com/api/2.0/export?project_id=2783792'
    params = {
        'from_date': '2022-10-11',
        'to_date': '2022-10-13',
        'limit': 100000,
    }
    response = requests.get(api_url, auth=(username, secret), params=params)
    return response


if __name__ == "__main__":
    response = get_mixpanel_data()

    print(response)

    print(response.text)

    f = open("mixpanel.csv", "w", encoding="utf-8", newline="")

    f.write(response.text)

    f.close()

