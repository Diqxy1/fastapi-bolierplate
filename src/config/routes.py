from fastapi import FastAPI

from src.users.routes import users_routes

def init_app(app: FastAPI):
    app.include_router(users_routes.router)