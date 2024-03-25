import requests

api_url = "http://server:5001"

def send_query(query):
    url = f"{api_url}/search?term={query}"
    res = requests.get(url)
    print(res.json())
    return res.json()

def fetch_data(task_id):
    url = f"{api_url}/fetch/{task_id}"
    res = requests.get(url)

    return res.json()