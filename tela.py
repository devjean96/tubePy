import PySimpleGUI as sg
from video import baixar_video

sg.theme('DarkAmber')

layout = [  [sg.Image(r'Python.svg.png')],
            [sg.Text('Aplicativo para Download de videos do Youtube')],
            [sg.Text('Insira o link para download:'), sg.InputText()],
            [sg.Text('Selecione o tipo de conversão'),sg.InputCombo(('mp4', 'mp3'), size=(20, 1), default_value='mp4')],
            [sg.Button('Baixar'), sg.Button('Cancelar')] ]

window = sg.Window('TubePy Download', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancelar':
        break
    print('You entered ', values[1], values[2])
    url = values[1]
    ext = values[2]
    if not url:
        window['TEST']
    baixar_video(values[1], values[2])

window.close()