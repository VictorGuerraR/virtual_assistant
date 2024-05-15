from pyowm import OWM
from pyowm.utils.config import get_default_config


def obtener_estado_clima():
    config_dict = get_default_config()
    config_dict['language'] = 'sp'  # Set language to Spanish

    owm = OWM('bb75e7b7a358b7cfeba7255881ba0c4a', config_dict)
    mgr = owm.weather_manager()

    # Search for current weather in Santa Catarina Pinula
    observation = mgr.weather_at_place('Santa Catarina Pinula, GT')
    w = observation.weather

    # Check if detailed status exists
    if hasattr(w, 'detailed_status'):
        status = w.detailed_status
    else:
        status = "No disponible"

    # Access temperature values from the dictionary
    temperature = w.temperature('celsius')
    temp = temperature['temp']
    temp_max = temperature['temp_max']
    temp_min = temperature['temp_min']
    feels_like = temperature['feels_like']

    # Construct the message using f-strings
    mensaje = f"Claro, el clima en Santa Catarina Pinula, Guatemala es: {status}.\nLa temperatura actual es {temp}°C.\nLa temperatura máxima es {temp_max}°C, la temperatura mínima es {temp_min}°C.\nPero se siente como {feels_like}°C."

    return mensaje
