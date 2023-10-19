# enviando e-mails com Python
import os
from dotenv import load_dotenv
from pathlib import Path
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

load_dotenv()

# caminho html
CAMINHO_HTML = Path(__file__).parent / 'aula185.html'

# dados do remetente e destinatário
remetente = os.getenv('FROM_EMAIL', '')
destinatario = remetente

# configurações SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')

# mensagem texto

with open(CAMINHO_HTML, 'r', encoding='utf8') as file:
    texto_file = file.read()
    template = Template(texto_file)
    texto_email = template.substitute(nome='jose')

# Transformar em MIMEMultipart
mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Assunto e-mail'

corpo_email = MIMEText(texto_email, 'html', 'utf-8')
mime_multipart.attach(corpo_email)

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)
    print('enviado')
