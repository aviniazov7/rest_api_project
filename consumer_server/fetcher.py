import requests
from .config import DATA_API_URL, DATA_API_KEY

def fetch_data_from_provider():
    headers = {"X-API-Key": DATA_API_KEY}
    try:
        response = requests.get(DATA_API_URL, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
