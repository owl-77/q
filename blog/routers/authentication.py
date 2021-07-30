from blog.token import create_access_token
from blog.hashing import Hash
from fastapi.exceptions import HTTPException
from pydantic import main
from blog import models
from fastapi import FastAPI,Depends,status
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from starlette.routing import Router
from .. import schemas,database,token,main
from ..hashing import Hash
from sqlalchemy.orm import Session



router=APIRouter(tags=['authentication'])



@router.post('/login')
def login(request:schemas.Login,db:Session=Depends(main.get)):
    user=db.query(models.User).filter(models.User.email== request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'invalid ')
    if not Hash.verify(user.password,request.password):
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'incorrect ')
    
    access_token =token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
