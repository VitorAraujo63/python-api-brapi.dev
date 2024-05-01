import json

dados = {
    "nome": "Vitor",
    "idade": "18",
    "cidade": "marilia"
}

with open("dados.json", "w") as file:
    json.dump(dados, file)
