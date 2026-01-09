from app.fetcher import fetch_csv
from app.parser import parse_csv, normalize
from threading import Lock

_CACHE = []
_LOCK = Lock()

def atualizar_cache():
    global _CACHE
    csv_text = fetch_csv()
    rows = parse_csv(csv_text)
    with _LOCK:
        _CACHE = normalize(rows)

def get_ativos():
    with _LOCK:
        return _CACHE
