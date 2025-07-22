import uvicorn
from Infrastructure.db import create_db_and_tables
from fastapi import FastAPI
from Application.Api import router as api_router

def initialize_app():
    create_db_and_tables() # Initialize the database

    app = FastAPI()
    app.include_router(api_router)
    return app
