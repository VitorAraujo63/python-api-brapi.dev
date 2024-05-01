from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme("Reddit")
layout = [
    [sg.Text('Escolha banco'),sg.Input(key='escolha')],
    [sg.Button('Pesquisar')]
]

# Janela

janela = sg.Window('Tela de pesquisa', layout)

# Ler os eventos

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSE:
        break
    if eventos == 'Pesquisar':
        if valores['escolha'] == 'ibo':
            print("Hello")