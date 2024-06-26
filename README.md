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

## Dependencies app

```bash
pip install -r requirements.txt
```

### With python venv:

```bash
python -m pip install -r requirements.txt
```

## Dependencies generator

```bash
pip install -r generator/requirements.txt
```

### With python venv:

```bash
python -m pip install -r generator/requirements.txt
```

## App

### Run app

```bash
uvicorn src.main:app --reload
```

### Building app docker image

``` bash
sudo docker build -t web-todo .
```

### Start app with docker

``` bash
sudo docker run --rm -p 80:80 -v "${PWD}/database":/database web-todo
```

## Generator

### Run

``` bash
python generator/generator.py
```

### Building generator docker image

``` bash
sudo docker build -t generator generator
```

### Start generator with docker

``` bash
sudo docker run --rm --network=host generator
```
