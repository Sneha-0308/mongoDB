from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from fastapi import FastAPI
import pymongo

app = FastAPI()

myclient = pymongo.MongoClient(
    "mongodb+srv://ruby:Sneha%4008@test.1p5iv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mydb = myclient["mydatabase"]
mycol = mydb["user"]


class User(BaseModel):
    name: str
    userid: str
    password: str


@app.post('/register/{name}')
def registers(request: User, name: str):
    res = {"response": "error"}
    if not mycol.find_one({'name': name}):
        request = jsonable_encoder(request)
        mycol.insert_one(request)
        res = {"response": "success"}
    else:
        res = {"response": "user already exists"}
    return res


@app.post('/login/{name}/{password}')
def logins(name: str, password: str):
    res = {"response": "error"}
    if mycol.find_one({'name': name}):
        if mycol.find_one({'password': password}):
            res = {"response": "success"}
        else:
            res = {"response": "Incorrect userid"}
    else:
        res = {"response": "Incorrect name"}
    return res
