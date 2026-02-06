from typing import Annotated
from fastapi import FastAPI, Query, Path, Body
from datetime import date

app = FastAPI()

@app.get('/')
def root():
    return {'message': 'Hello world!'}

@app.get('/users')
def read_users():
    return [{'user': 'Christian'}, {'user': 'Kerttuli'}]

@app.post('/users')
def create_user():
    pass

@app.get('/users/{user_id}')
def read_user(user_id: int):
    # print(type(user_id))
    return {'user_id': user_id, 'name': 'Christian'}

@app.get('/diary/{day}/{user}')
def get_diary_date(
    day: date,
    user: str,
    start_date: date,
    end_date: date,
    q: str | None = 'aaaa',
    ):
    return {'year': day.year, 'month': day.month, 'day': day.day, 'query': q}

@app.get('/sum/')
def sum_numbers(op1: int, op2: int):
    return {'result': op1+op2}

from enum import Enum
class Color(str, Enum):
    red = 'red'
    green = 'green'

@app.get('/test')
def test(val: bool, val2: Color, q: Annotated[int, Query(
    ge = 0,
    le = 10,
    description='Some value between 0 and 10',
    examples=[0, 5, 9],
    title='Integer query'
)]):
    return {'value': val, 'value2': val2, 'q': q}



