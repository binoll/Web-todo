# Web todo

## Overview

This is a web-based task management application. 
The application is written using the "FastAPI" framework.
There is also a "generator" script that creates 20 todos.
The handles were tested using "postman".

## Documentation

[FastAPI tutorial](https://fastapi.tiangolo.com/ru/tutorial/)\
[Swagger UI documentation](http://127.0.0.1:8000/docs)\
[ReDoc documentation](http://127.0.0.1:8000/redoc)

## Dependencies

### Install app dependencies

```bash
python -m pip install -r requirements.txt
```

### Install generator dependencies

```bash
python -m pip install -r generator/requirements.txt
```

## Run

### Run app

```bash
uvicorn src.main:app --reload
```

### Run generator

``` bash
python generator/generator.py
```

## Run with docker

### Run app

``` bash
sudo docker build -t web-todo .
```

``` bash
sudo docker run --rm -p 8000:8000 -v "${PWD}/database":/database web-todo
```

### Run generator

``` bash
sudo docker build -t generator generator
```
``` bash
sudo docker run --rm --network=host generator
```
