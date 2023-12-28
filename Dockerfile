FROM python:3.10-slim

COPY requirements.txt /requirements.txt
COPY source /source
COPY web /web

RUN pip install --no-cache-dir --upgrade -r requirements.txt

ENTRYPOINT ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--reload", "--port", "80"]