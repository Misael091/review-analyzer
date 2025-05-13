from fastapi import FastAPI
from app.routers import review, auth

app = FastAPI(title="Review Analyzer")

app.include_router(review.router, prefix="/api/review")
app.include_router(auth.router) 
