import os
import subprocess


def buscar_archivo_en_pc(nombre_archivo):
    for root, dirs, files in os.walk(r'C:\\'):
        for file in files:
            if nombre_archivo.lower() == os.path.splitext(file)[0].lower():
                return os.path.join(root, file)
            elif nombre_archivo.lower() == os.path.splitext(os.path.basename(file))[0].lower():
                return os.path.join(root, file)
    return None


def abrir_archivo_con_explorador(ruta):
    if ruta:
        if os.name == 'nt':  # Comprobación de si estamos en Windows
            subprocess.Popen(['explorer', ruta], shell=True)
            return 'Archivo encontrado'
        else:
            return "Lo siento, esta función solo es compatible con Windows."
    else:
        return "El archivo no se encontró en la PC."


def manangment_explorador(nombre):
    print(nombre)
    ruta_del_archivo = buscar_archivo_en_pc(nombre_archivo=nombre.strip())
    print(ruta_del_archivo)
    mesaje = abrir_archivo_con_explorador(ruta=ruta_del_archivo)
    return mesaje
