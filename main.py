from fastapi import FastAPI
from db import Some_db
from pydantic import BaseModel

app = FastAPI()


class Multiple(BaseModel):
    x1: int
    x2: int


@app.put('/mul')
def multiple(x1:int =None, x2: int =None):
    # x1, x2 = tuple(map(int, (x1, x2)))
    Some_db.put_db(x1, x2)
    return x1 * x2,


@app.get('/result')
def results():
    return Some_db.database


@app.delete('/delete')
def delete(pk=None):
    Some_db.delete(int(pk))
    return 'Done'
