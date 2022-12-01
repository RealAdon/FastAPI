from fastapi import FastAPI
from utils import zefix

app = FastAPI()

@app.get('/')
def index():
    return {'data':{'name':'Elia'}}

@app.get('/zefix')
def getZefix(uid: str):
    return zefix.search(uid)