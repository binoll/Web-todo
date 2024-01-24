# Description

This is a web-based task management application.

## Documentation

[FastAPI tutorial](https://fastapi.tiangolo.com/ru/tutorial/)\
[Swagger UI documentation](http://127.0.0.1:8000/docs)\
[ReDoc documentation](http://127.0.0.1:8000/redoc)

## Dependencies

```bash
python -m pip install -r requirements.txt
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

## Scripts

### Run

``` bash
python generator/generator.py 
```

### Building script docker image

``` bash
sudo docker build -t generator generator
```

### Start script with docker

``` bash
sudo docker run --rm --network=host generator
```
