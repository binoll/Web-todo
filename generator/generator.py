"""
Generator script
"""
import lorem
import requests

GENERATION_COUNT = 20
LOCALHOST_IP = '127.0.0.1'
PORT = 8000
URL = f'http://{LOCALHOST_IP}:{PORT}/add'


def generate_title():
    """
    Generates a random title
    """
    return lorem.sentence()


for i in range(GENERATION_COUNT):
    payload = {
        'title': generate_title()
    }
    response = requests.post(URL, data=payload)
