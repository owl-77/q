from typing import Optional, Text
from fastapi import FastAPI
from fastapi.param_functions import Body
from pydantic import BaseModel

app=FastAPI()


@app.get('/blog')
def index(limit=20,published:bool=True,sort:Optional[str]=None):

    if published:
        return { 'data': f'blog list {limit}' }
    else:
        return { 'data': f'blog unlist {limit}' }

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all of them'}

@app.get('/blog/{id}')
def show(id:int):
    return {'data' : id }

@app.get('/blog/{id}/comments')

def comment(id):
    return {'data': {'1','2'}}

#request body for send data from clinet to api in post method
class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]


@app.post('/blog')
def create_blog(blog:Blog):
    
    return {'data': f'blog created {blog.title}'}