"""
Основной модуль FastAPI для управления задачами (todos).
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
async def home(request: Request, database: Session = Depends(get_db)) -> templates.TemplateResponse:
    """Главная страница.

    Args:
        request (Request): Запрос FastAPI.
        database (Session): Сессия базы данных.

    Returns:
        templates.TemplateResponse: HTML-страница с формой добавления задачи и списком задач.
    """
    logger.info('Открытие главной страницы')
    todo = database.query(models.Todo).order_by(models.Todo.id.desc())

    return templates.TemplateResponse('add.html', {'request': request, 'todos': todo, 'tags': Tags})


@app.get('/list')
async def list(request: Request, database: Session = Depends(get_db),
               page: int = Query(default=0, ge=0),
               page_limit: int = Query(default=10, gt=0)) -> templates.TemplateResponse:
    """Страница списка задач с пагинацией.

    Args:
        request (Request): Запрос FastAPI.
        database (Session): Сессия базы данных.
        page (int): Номер страницы (по умолчанию 0).
        page_limit (int): Количество задач на странице (по умолчанию 10).

    Returns:
        templates.TemplateResponse: HTML-страница с пагинированным списком задач.
    """
    todo = database.query(models.Todo).order_by(models.Todo.id.desc())
    total_todos = todo.count()
    total_pages = math.ceil(total_todos / page_limit)

    start_idx = page * page_limit
    end_idx = (page + 1) * page_limit
    todos_on_page = todo.slice(start_idx, end_idx).all()

    return templates.TemplateResponse('list.html',
                                      {'request': request, 'total_todos': total_todos, 'todos': todos_on_page,
                                       'page': page, 'total_pages': total_pages})


@app.post('/add')
async def add(database: Session = Depends(get_db),
              title: str = Form(default='', min_length=1, max_length=500),
              tag: str = Form(default=Tags.plans.name),
              description: str = Form(default='', max_length=10000)) -> RedirectResponse:
    """Добавление новой задачи.

    Args:
        database (Session): Сессия базы данных.
        title (str): Заголовок задачи.
        tag (str): Тег задачи (по умолчанию 'plans').
        description (str): Описание задачи.

    Returns:
        RedirectResponse: Перенаправление на главную страницу.

    Raises:
        HTTPException: Если заголовок задачи пуст.
    """
    if not title:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='Поле заголовка пусто!')

    todo = models.Todo(title=title, description=description, tag=tag)

    database.add(todo)
    database.commit()

    logger.info(f'Создание задачи: {todo}')

    return RedirectResponse(url=app.url_path_for('home'), status_code=status.HTTP_303_SEE_OTHER)


@app.get('/edit/{todo_id}')
async def edit_get(request: Request, database: Session = Depends(get_db),
                   todo_id: int = Path(gt=0)) -> templates.TemplateResponse:
    """Страница редактирования существующей задачи.

    Args:
        request (Request): Запрос FastAPI.
        database (Session): Сессия базы данных.
        todo_id (int): Идентификатор задачи.

    Returns:
        templates.TemplateResponse: HTML-страница для редактирования задачи.
    """
    todo = database.query(models.Todo).filter(models.Todo.id == todo_id).first()

    logger.info(f'Редактирование задачи: {todo}.')

    return templates.TemplateResponse('edit.html', {'request': request, 'todo': todo, 'tags': Tags})


@app.post('/edit/{todo_id}')
async def edit_post(database: Session = Depends(get_db),
                    todo_id: int = Path(gt=0),
                    title: str = Form(default='', max_length=500),
                    description: str = Form(default='', max_length=10000),
                    tag: str = Form(default=Tags.plans.name),
                    completed: bool = Form(default=False)) -> RedirectResponse:
    """Редактирование существующей задачи.

    Args:
        database (Session): Сессия базы данных.
        todo_id (int): Идентификатор задачи.
        title (str): Новый заголовок задачи.
        description (str): Новое описание задачи.
        tag (str): Новый тег задачи.
        completed (bool): Статус выполнения задачи.

    Returns:
        RedirectResponse: Перенаправление на страницу списка задач.

    Raises:
        HTTPException: Если заголовок задачи пуст.
    """
    if not title:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='Поле заголовка пусто!')

    todo = database.query(models.Todo).filter(models.Todo.id == todo_id).first()

    logger.info(f'Задача изменена: {todo}.')

    if title:
        todo.title = title
    if description:
        todo.description = description
    if tag:
        todo.tag = tag
    if completed:
        todo.completed = True
    else:
        todo.completed = False

    database.commit()

    return RedirectResponse(url=app.url_path_for('list'), status_code=status.HTTP_303_SEE_OTHER)


@app.post('/delete/{todo_id}')
async def delete(todo_id: int = Path(gt=0), database: Session = Depends(get_db)) -> RedirectResponse:
    """Удаление существующей задачи.

    Args:
        todo_id (int): Идентификатор задачи.
        database (Session): Сессия базы данных.

    Returns:
        RedirectResponse: Перенаправление на страницу списка задач.
    """
    todo = database.query(models.Todo).filter(models.Todo.id == todo_id).first()

    logger.info(f'Удаление задачи: {todo}.')

    if todo is None:
        logger.warning(f'Задача не существует: {todo}.')
        return RedirectResponse(url=app.url_path_for('list'), status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

    database.delete(todo)
    database.commit()

    return RedirectResponse(url=app.url_path_for('list'), status_code=status.HTTP_303_SEE_OTHER)
