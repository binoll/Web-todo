"""
Скрипт для генерации случайных заголовков и отправки их на указанный API-эндпоинт.
"""

import lorem
import requests

GENERATION_COUNT = 20  # Количество заголовков для генерации
LOCALHOST_IP = '127.0.0.1'
PORT = 8000
URL = f'http://{LOCALHOST_IP}:{PORT}/add'


def generate_title() -> str:
    """Генерирует случайный заголовок с использованием библиотеки lorem.

    Возвращает:
        str: Случайно сгенерированный заголовок в виде предложения.
    """
    return lorem.sentence()


def send_title_to_api(url: str, title: str) -> requests.Response:
    """Отправляет заголовок на указанный API-эндпоинт.

    Аргументы:
        url (str): URL API-эндпоинта.
        title (str): Заголовок для отправки.

    Возвращает:
        requests.Response: Объект ответа от API.
    """
    payload = {'title': title}
    response = requests.post(url, data=payload)
    return response
