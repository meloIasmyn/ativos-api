import time
from threading import Lock
from app.fetcher import fetch_csv
from app.parser import parse_csv, normalize

_CACHE = []
_LAST_UPDATE = 0
_LOCK = Lock()

TTL = 60

def get_ativos():
    global _CACHE, _LAST_UPDATE

    now = time.time()

    with _LOCK:
        cache_expirado = (now - _LAST_UPDATE) > TTL
        cache_vazio = not _CACHE

        if cache_expirado or cache_vazio:
            print("Atualizando cache...")
            try:
                csv_text = fetch_csv()
                rows = parse_csv(csv_text)
                _CACHE = normalize(rows)
                _LAST_UPDATE = now
            except Exception as e:
                print("Erro ao atualizar cache:", e)
                # mantém cache antigo se existir

        return _CACHE
