from fastapi import APIRouter, HTTPException, Header

routers = APIRouter()

@routers.get("/")
def read_root():
    return {"message": "FAST API World"}