# ATIVOS API

API em Python (FastAPI) que lê uma planilha do Google Sheets (CSV público) e disponibiliza os dados em formato JSON para consumo por aplicações web.

A planilha é sincronizada automaticamente e as alterações refletem na API sem necessidade de restart.

## O que essa API faz

- Lê dados de uma planilha Google Sheets
- Normaliza os dados
- Calcula 4% a mais no preço
- Mantém cache em memória
- Atualiza automaticamente a cada 5 minutos
- Disponibiliza endpoint HTTP em JSON

## Endpoint

`GET /ativos`

Retorna a lista de ativos.

**Exemplo:**

```json
[
  {
    "nome_bm": "BM Exemplo",
    "preco": 1000.0,
    "preco_com_4": 1040.0,
    "informacoes": "Conta ativa",
    "valor_rodado_contas_ativas": "R$ 30.000",
    "ano_criacao": "2023"
  }
]```

# COMO RODAR LOCALMENTE

## 1. Criar ambiente virtual
    python -m venv venv

## 2. Ativar ambiente virtual
    venv\Scripts\activate

## 3. Instalar dependências
    pip install -r requirements.txt

## 4. Subir a API
    uvicorn app.main:app

# URLs LOCAIS
    - API: http://127.0.0.1:8000/ativos
    - Documentação automática: http://127.0.0.1:8000/docs

# OBSERVAÇÕES
*   O JSON é gerado dinamicamente no endpoint.
*   Não existe banco de dados.
*   O cache fica apenas em memória.
*   Alterações na planilha refletem automaticamente na API.

