import requests

CSV_URL = "https://docs.google.com/spreadsheets/d/1nZgsrYbhA76tMme8ZCaJqb_Cmj0o1pNZeyTYqChJzjw/export?format=csv"

def fetch_csv():
    resp = requests.get(CSV_URL, timeout=10)
    resp.raise_for_status()

    resp.encoding = "utf-8"

    return resp.text
    