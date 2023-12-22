FROM python:3.12

COPY requirements.txt /requirements.txt

ARG PROXY
RUN if [ -z "$PROXY" ]; then \
         pip install --no-cache-dir --upgrade -r requirements.txt; \
    else \
        pip install --no-cache-dir --proxy "$PROXY" --upgrade -r requirements.txt; \
    fi

COPY source /source
COPY web /web

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--reload", "--port", "80"]
