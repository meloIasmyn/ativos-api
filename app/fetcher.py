import requests

CSV_URL = "https://docs.google.com/spreadsheets/d/1qvkXlgZ4g1aNu1i7aaNrNo1siwEQh_eQTK3z6T5zvAk/export?format=csv"

def fetch_csv():
    resp = requests.get(CSV_URL, timeout=10)
    resp.raise_for_status()

    resp.encoding = "utf-8"

    return resp.text
    