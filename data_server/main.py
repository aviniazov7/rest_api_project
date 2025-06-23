from fastapi import FastAPI
from . import routes

app = FastAPI(
    title="Data Provider API",
    description="Provides protected data via Basic Auth and API Key",
    version="1.0.0"
)

app.include_router(routes.router)
