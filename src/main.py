"""
Main
"""
import math

from fastapi import FastAPI, Request, Depends, Form, Path, status, HTTPException, Query
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from loguru import logger
from sqlalchemy.orm import Session

import src.models as models
from src.database import init_db, get_db
from src.tags import Tags

app = FastAPI()
templates = Jinja2Templates(directory='web/html')

init_db()
app.mount('/web', StaticFiles(directory='web'), name='web')
logger = logger.opt(colors=True)


@app.get('/')
async def home(request: Request,
               database: Session = Depends(get_db)) -> templates.TemplateResponse:
	"""
	Main page
    """
	logger.info('Opening home page')
	task = database.query(models.Task).order_by(models.Task.id.desc())
	
	return templates.TemplateResponse('add.html', {'request': request, 'tasks': task, 'tags': Tags})


@app.get('/list')
async def list(request: Request,
               database: Session = Depends(get_db),
               page: int = Query(default=0, ge=0),
               page_limit: int = Query(default=10, gt=0)) -> templates.TemplateResponse:
	"""
	List page
    """
	tasks = database.query(models.Task).order_by(models.Task.id.desc())
	total_tasks = tasks.count()
	total_pages = math.ceil(total_tasks / page_limit)
	
	start_idx = page * page_limit
	end_idx = (page + 1) * page_limit
	tasks_on_page = tasks.slice(start_idx, end_idx).all()
	
	return templates.TemplateResponse('list.html', {'request': request, 'tasks': tasks_on_page, 'page': page,
	                                                'total_pages': total_pages})


@app.post('/add')
async def add(database: Session = Depends(get_db),
              title: str = Form(default='', min_length=1, max_length=500),
              tag: str = Form(default=Tags.plans.name),
              description: str = Form(default='', max_length=10000)) -> RedirectResponse:
	"""
	Add new task
	"""
	if not title:
		raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Title field is empty!")
	
	task = models.Task(title=title, description=description, tag=tag)
	
	database.add(task)
	database.commit()
	
	logger.info(f'Creating task: {task}')
	
	return RedirectResponse(url=app.url_path_for('home'), status_code=status.HTTP_303_SEE_OTHER)


@app.get('/edit/{id}')
async def edit_get(request: Request,
                   database: Session = Depends(get_db),
                   id: int = Path(gt=0)) -> RedirectResponse:
	"""
	Edit existed task
	"""
	task = database.query(models.Task).filter(models.Task.id == id).first()
	
	logger.info(f'Editing task: {task}.')
	
	return templates.TemplateResponse('edit.html', {'request': request, 'task': task, 'tags': Tags})


@app.post('/edit/{id}')
async def edit_post(database: Session = Depends(get_db),
                    id: int = Path(gt=0),
                    title: str = Form(default='', max_length=500),
                    description: str = Form(default='', max_length=10000),
                    tag: str = Form(default=Tags.plans.name),
                    completed: bool = Form(default=False)):
	"""
	Edit existed task
	"""
	if not title:
		raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Title field is empty!")
	
	task = database.query(models.Task).filter(models.Task.id == id).first()
	
	logger.info(f'The task has been changed: {task}.')
	
	if title:
		task.title = title
	if description:
		task.description = description
	if tag:
		task.tag = tag
	if completed:
		task.completed = True
	else:
		task.completed = False
	
	database.commit()
	
	return RedirectResponse(url=app.url_path_for('list'), status_code=status.HTTP_303_SEE_OTHER)


@app.get('/delete/{id}')
async def delete(id: int = Path(gt=0),
                 database: Session = Depends(get_db)):
	"""
	Delete existed task
	"""
	task = database.query(models.Task).filter(models.Task.id == id).first()
	
	logger.info(f'Deleting the task: {task}.')
	
	if task is None:
		logger.warning(f'This task does not exist: {task}.')
		return RedirectResponse(url=app.url_path_for('list'), status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
	
	database.delete(task)
	database.commit()
	
	return RedirectResponse(url=app.url_path_for('list'), status_code=status.HTTP_303_SEE_OTHER)
