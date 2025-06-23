from fastapi import FastAPI
from .fetcher import fetch_data_from_provider

app = FastAPI(
    title="Consumer API",
    description="Fetches protected data from Data Provider using API Key",
    version="1.0.0"
)

@app.get("/fetch-data", summary="Fetch data from provider")
def fetch_data():
    return fetch_data_from_provider()
