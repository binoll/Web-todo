FROM python:3.12-slim

COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY generator.py /generator.py

CMD ["python", "generator.py"]