from fastapi import FastAPI
from app.api.router import router
from app.api.auth import router as auth_router

app = FastAPI()

app.include_router(router, prefix="/api")
app.include_router(auth_router, prefix="/auth")
