import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()


def enviar_correo(message):
    # create message object instance
    msg = MIMEMultipart()
    # setup the parameters of the message
    password = os.getenv("CLAVE")
    msg['From'] = os.getenv("CORREO")
    msg['To'] = "hugo23527@gmail.com"
    msg['Subject'] = "Subscription"
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    # create server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
    return 'Correo enviado con éxito'


# Llamada a la función para enviar correo
enviar_correo()
