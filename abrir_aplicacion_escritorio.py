import os
import subprocess


def buscar_ejecutable(nombre_aplicacion):
    for root, dirs, files in os.walk(r'C:\\'):
        for file in files:
            # Verificar si el archivo tiene la extensión .exe y si el nombre del archivo coincide exactamente con el texto buscado
            if file.lower() == (nombre_aplicacion.lower() + ".exe"):
                ruta = os.path.join(root, file)
                return ruta

    return None


def lanzar_ejecutable(nombre):
    ruta_ejecutable = buscar_ejecutable(nombre_aplicacion=nombre.strip())
    if ruta_ejecutable:
        subprocess.Popen(ruta_ejecutable)
        return f"Se encontró el ejecutable de {nombre}"
    else:
        return f"No se encontró el ejecutable de {nombre}"
