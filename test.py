from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from fastapi import FastAPI
import pymongo

test = FastAPI()

myclient = pymongo.MongoClient(
    "mongodb+srv://ruby:Sneha%4008@test.1p5iv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mydb = myclient["mydatabase"]
mycol = mydb["user"]


class User(BaseModel):
    name: str
    userid: str
    password: str


@test.post('/register/{name}')
def registers(request: User, name: str):
    if not mycol.find_one({'name': name}):
        request = jsonable_encoder(request)
        mycol.insert_one(request)
        res = {"response": "success"}
    else:
        res = {"response": "user already exists"}
    return res


@test.post('/login/{name}/{password}')
def login(name: str, password: str):
    nameid = mycol.find_one({"name": name})
    passwordid = mycol.find_one({"password": password})
    if nameid is None:
        res = {"response": "incorrect name"}
    elif passwordid is None:
        res = {"response": "incorrect password"}
    else:
        res = {"response": "Success"}
    return res




