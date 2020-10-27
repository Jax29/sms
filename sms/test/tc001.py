import requests
import pprint

payload = {'username': 'jax', 'password': '88888888'}

response = requests.post('http://localhost:8000/api/mgr/signin', data=payload)

pprint.pprint(response.json())
