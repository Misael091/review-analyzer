from fastapi import APIRouter
from app.services.auth import create_access_token

router = APIRouter()

@router.post("/token")
def login():
    token = create_access_token({"sub": "example_user"})
    return {"access_token": token, "token_type": "bearer"}