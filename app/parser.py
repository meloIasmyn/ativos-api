import csv
from io import StringIO

def parse_csv(csv_text):
    reader = csv.reader(StringIO(csv_text))
    return list(reader)

def normalize(rows):
    ativos = []

    for row in rows:
        if len(row) < 5:
            continue

        preco_raw = row[1].strip()

        try:
            preco = float(
                preco_raw
                .replace("R$", "")
                .replace(".", "")
                .replace(",", ".")
            )
        except:
            continue

        ativos.append({
            "nome_bm": row[0].strip(),
            "preco": preco,
            "preco_com_4": round(preco * 1.04, 2),
            "informacoes": row[2].strip(),
            "valor_rodado_contas_ativas": row[3].strip(),
            "ano_criacao": row[4].strip(),
        })

    return ativos
