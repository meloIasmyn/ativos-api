import time
from threading import Lock
from app.fetcher import fetch_csv
from app.parser import parse_csv, normalize

_CACHE = []
_LAST_UPDATE = 0
_LOCK = Lock()

TTL = 30  

def get_ativos():
    global _CACHE, _LAST_UPDATE

    now = time.time()

    with _LOCK:
        if now - _LAST_UPDATE > TTL:
            print("TTL expirado, atualizando cache...")
            csv_text = fetch_csv()
            rows = parse_csv(csv_text)
            _CACHE = normalize(rows)
            _LAST_UPDATE = now
        else:
            print("Cache ainda válido")

        return _CACHE
