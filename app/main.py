from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.service import get_ativos, atualizar_cache
import threading
import time
import os

ENABLE_POLLING = os.getenv("ENABLE_POLLING", "true") == "true"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # em produção pode restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def polling():
    while True:
        try:
            print("Atualizando cache...")
            atualizar_cache()
            print("Cache atualizado com sucesso.")
        except Exception as e:
            print("Erro ao atualizar cache:", e)
        time.sleep(300)

@app.on_event("startup")
def startup():
    atualizar_cache()  # primeira carga
    if ENABLE_POLLING:
        thread = threading.Thread(target=polling, daemon=True)
        thread.start()

@app.get("/ativos")
def ativos():
    return get_ativos()
