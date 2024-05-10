import time
import PySimpleGUI as pySG
import virtual_assistant_app as asistente

# pySG.theme('Dark Black')

layout = [
    [pySG.Image(
        filename='./images/bot.png',
        key='_IMAGE_',
        size=(256, 256)
    )],
    [],
    [pySG.Button(
        '',
        image_filename='./images/not-listen-microphone.png',
        button_color=(pySG.theme_background_color(), pySG.theme_background_color()),
        border_width=0,
        key='_MIC_',
        image_size=(51, 51),
        size=(5, 5)
    ), pySG.Button('Cancel')],
]

window = pySG.Window(title="Asistente", layout=layout)

while True:
    event, values = window.read(timeout=10)

    if event == '_MIC_':
        asistente.run()
    elif event == pySG.WINDOW_CLOSED or event == 'Cancel':
        break

    # Actualiza la imagen del micrófono según el valor de escuchando
    if asistente.escuchando:
        window['_MIC_'].update(image_filename='./images/listen-microphone.png')
    else:
        window['_MIC_'].update(image_filename='./images/not-listen-microphone.png')
        break

window.close()
