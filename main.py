from fastapi import FastAPI
from backend.src.routers import router

app = FastAPI()

app.include_router(router, prefix="/api")
