import lorem
import requests

GENERATION_COUNT = 20
url = 'http://localhost:8000/add'


def generate_title():
	return lorem.sentence()


for _ in range(GENERATION_COUNT):
	payload = {
		'title': generate_title()
	}
	response = requests.post(url, data=payload)
	
	if response.status_code != 200:
		print(f"Error sending POST request: {response.status_code}")