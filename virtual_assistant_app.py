import datetime as time
import random

import pyjokes as chistes
import pyttsx3
import pywhatkit
import speech_recognition as speech
import wikipedia

import clima_app as clima_app
import correo_app as correo

# Nombre del asistente
name = 'nombre'  # TODO: Debes ingresar el nombre de tu asistente aquí

# Permite reconocer la voz
listener = speech.Recognizer()

# Permite hablar con el usuario
engine = pyttsx3.init()

engine.setProperty('voice', 'spanish')
#
# rate = engine.getProperty('rate')
# engine.setProperty('rate', rate - 100)
#
# volume = engine.getProperty('volume')
# engine.setProperty('volume', volume + 0.50)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[4].id)

# Configura el idioma de Wikipedia
wikipedia.set_lang('es')

# Traducción de los meses
spanish_month = {
    'January': 'Enero',
    'February': 'Febrero',
    'March': 'Marzo',
    'April': 'Abril',
    'May': 'Mayo',
    'June': 'Junio',
    'July': 'Julio',
    'August': 'Agosto',
    'September': 'Septiembre',
    'October': 'Octubre',
    'November': 'Noviembre',
    'December': 'Diciembre'
}

observadores = []


def registrar_observador(observador):
    observadores.append(observador)


def notificar_cambio_escucha(estado):
    for observador in observadores:
        observador.actualizar_escucha(estado)


# Funciones de comandos
def reproducir_musica(music):
    talk('Reproduciendo ' + music)
    pywhatkit.playonyt(music)


def indicar_hora(text):
    hora = time.datetime.now().strftime('%I:%M %p')
    talk('Son las ' + hora)


def indicar_fecha(text):
    fecha = time.datetime.now().strftime('%d-%h-%Y')
    talk('La fecha es: ' + fecha)


def indicar_dia(text):
    dia = time.datetime.now().strftime('%d')
    talk('Hoy es el día ' + dia)


def indicar_mes(text):
    mes = time.datetime.now().strftime('%B')
    mes_translate = spanish_month.get(mes, mes)  # Si el mes no está en el diccionario, devuelve el nombre en inglés
    talk('Estamos en el mes de ' + mes_translate)


def indicar_anio(text):
    year = time.datetime.now().strftime('%Y')
    talk('Estamos en el ' + year)


def buscar_wikipedia(consulta):
    talk('Buscando en Wikipedia ' + consulta)
    try:
        resultado = wikipedia.summary(consulta, sentences=3)
        talk(resultado)
    except wikipedia.exceptions.DisambiguationError as e:
        talk('La búsqueda es ambigua. Por favor, sé más específico.')
    except wikipedia.exceptions.PageError as e:
        talk('No se encontró ninguna página relacionada. Por favor, intenta con otro término.')


def buscar_google(consulta):
    talk('Buscando en Google ' + consulta)
    pywhatkit.search(consulta)


def contar_chiste(text):
    chiste = chistes.get_joke(language='es', category='neutral')
    talk(chiste)


def indicar_clima(text):
    clima = clima_app.obtener_estado_clima()
    talk(clima)


def enviar_correo(text):
    resultado = correo.enviar_correo(text)
    talk(resultado)


def comando_no_entendido(text):
    talk('Disculpa, no te entiendo')


# Diccionario de comandos
comandos = {
    'reproduce': reproducir_musica,
    'hora': indicar_hora,
    'fecha': indicar_fecha,
    'día': indicar_dia,
    'mes': indicar_mes,
    'año': indicar_anio,
    'busca en wikipedia': buscar_wikipedia,
    'busca en google': buscar_google,
    'chiste': contar_chiste,
    'clima': indicar_clima,
    'correo': enviar_correo
}


# Genera un mensaje aleatorio para el usuario
def prompt_usuario():
    lista = ['Te escucho', 'Dime tu orden', 'Estoy escuchándote', 'Dime']
    return random.choice(lista)


# Método que permite al asistente hablar
def talk(text):
    engine.say(text)
    engine.runAndWait()


# Método que permite al asistente escuchar
def listen():
    global listener  # Asegurarse de que listener sea global
    recognizer = ""
    try:
        with speech.Microphone() as source:
            print('Escuchando...')
            talk(prompt_usuario())
            voice = listener.record(source, duration=10)
            notificar_cambio_escucha(estado=False)
            print('Reconociendo voz...')
            recognizer = listener.recognize_google(voice, language='es-MX')
            recognizer = recognizer.lower()

            if name in recognizer:
                recognizer = recognizer.replace(name, '')

    except speech.UnknownValueError:
        recognizer = 'No se pudo entender el audio'
    except speech.RequestError:
        recognizer = 'Error en la solicitud de reconocimiento de voz. Verifique su conexión a Internet.'
    except Exception as e:
        print('Error:', e)
    return recognizer


# Método que ejecuta al asistente
def run():
    notificar_cambio_escucha(estado=True)
    recognizer = listen()

    for comando, funcion in comandos.items():
        if comando in recognizer:
            funcion(recognizer.replace(comando, ''))
            break
    else:
        comando_no_entendido('No se entendio')
