from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.services.review_service import analyze_review
from app.services.auth import verify_token, get_current_user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter()

@router.post("/", dependencies=[Depends(get_current_user)])
def review_endpoint(payload: dict):
    content = payload.get("content", "")
    return analyze_review(content)
