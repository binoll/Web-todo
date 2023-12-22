## Dependencies

```bash
pip install --user -r requirements.txt
```

## Run

```bash
uvicorn source.main:todo_app --reload
```

## Documentation

[FastAPI tutorial](https://fastapi.tiangolo.com/ru/tutorial/)\
[Swagger UI documentation](http://127.0.0.1:8000/docs)\
[ReDoc documentation](http://127.0.0.1:8000/redoc)

## Docker

### Building docker image

``` bash
docker build -t lw1 .
```

### Start docker

Release

``` bash
docker run --rm -p 80:80 -v "${PWD}/database":/database lw1
```

Debug

``` bash
docker run --rm -p 80:80 -v "${PWD}/source":/source -v "${PWD}/database":/database lw1

## Scripts

### Run

``` bash
python generator/generator.py 
```

### Building script docker image

``` bash
docker build -t lw1 scripts/generator
```

### Start script with docker

``` bash
docker run --rm --network=host lw1
```