from fastapi import FastAPI
from app.service import get_ativos

app = FastAPI(
    title="ATIVOS API",
    description="API para disponibilização de ativos via Google Sheets",
    version="1.0.0"
)

@app.get("/ativos")
def ativos():
    return get_ativos()
