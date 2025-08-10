import requests

API_KEY = "7Hm0KVhv6IXpNIOD1KvPQw==QpGHB1IRQiRAgeCE"

def fetch_data(animal_name):
    """
    Makes an API call to get information about an animal.
    Returns a list of animal data in JSON format or None in case of an error
    """
    api_url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
        return None