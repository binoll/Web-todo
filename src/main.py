"""
Main
"""
import src.models as models

from loguru import logger
from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from src.database import init_db, get_db

app = FastAPI()
templates = Jinja2Templates(directory='web/html')

init_db()
app.mount('/css', StaticFiles(directory='web'), name='css')
app.mount('/js', StaticFiles(directory='web'), name='js')
logger = logger.opt(colors=True)


@app.get('/')
async def home(request: Request,
               database: Session = Depends(get_db)):
	"""
	Main page
    """
	logger.info('The home page is open')
	todos = database.query(models.Todo).order_by(models.Todo.id.desc())

	return templates.TemplateResponse('index.html', {'request': request, 'todos': todos})
