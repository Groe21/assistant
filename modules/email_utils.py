import smtplib

def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('tu_correo@gmail.com', 'tu_contraseña')
    server.sendmail('tu_correo@gmail.com', to, content)
    server.close()
