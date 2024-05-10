import time
import PySimpleGUI as pySG
import virtual_assistant_app as asistente


class Observador:
    def actualizar_escucha(self, estado):
        # Actualiza la imagen del micrófono según el valor de asistente.escuchando
        if estado:
            window['_MIC_'].update(image_filename='./images/listen-microphone.png')
            window.refresh()
        else:
            window['_MIC_'].update(image_filename='./images/not-listen-microphone.png')
            window.refresh()


# Crear una instancia de la clase Observador
observador = Observador()


def init():
    # tu código de inicialización del GUI aquí
    asistente.registrar_observador(observador)

init()


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

window.close()
