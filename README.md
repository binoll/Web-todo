# Description
This is a web-based task management application.

## Documentation
[FastAPI tutorial](https://fastapi.tiangolo.com/ru/tutorial/)\
[Swagger UI documentation](http://127.0.0.1:8000/docs)\
[ReDoc documentation](http://127.0.0.1:8000/redoc)

## Dependencies
```bash
pip install --user -r requirements.txt
```

## Run
```bash
uvicorn source.main:todo_app --reload
```

## Docker
### Building docker image
``` bash
sudo docker build -t web-todo .
```

### Start docker
``` bash
docker run --rm -p 80:80 -v "${PWD}/database":/database web-todo
```

## Scripts
### Run
``` bash
python generator/generator.py 
```

### Building script docker image
``` bash
docker build -t web-todo generator generator
```

### Start script with docker
``` bash
docker run --rm --network=host web-todo
```