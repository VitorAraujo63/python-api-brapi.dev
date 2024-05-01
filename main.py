import requests
import json

tickers = input('')
token = 'bDL6Hg9skc5MCadatdFhby'
request = requests.get(f'https://brapi.dev/api/quote/list?token={token}&search={tickers}')

dados = request.json()


with open("registro.json", "w") as arquivo:
    json.dump(dados, arquivo)

