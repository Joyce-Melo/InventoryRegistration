#Definir mensagens a serem enviadas 
# -> Mensagem de sucesso -> Definido se ocorreu tudo bem, mandado após cada cadastro enviando junto o código do produto
# -> Mensagem de erro -> Caso um produto não foi cadastrado -> Enviando também o código do produto
# -> Interrupção da execução -> Qualquer erro não esperado, que interrompa ou umpeça a execução -> Não é necessário enviar o código, visto que pode ser um erro em qualquer parte
# ->  Email Final -> Email final, informa que o bot finalizou a execução, envia o log e eo arquivo preenchido em anexo
# -> Ps: o bot deve também fazer upload do arquivo na pasta output do Google Drive

import os
import environ
import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders 
import openpyxl

env = environ.Env()
environ.Env().read_env()

workbook = openpyxl.load_workbook('ParametersFiles\\EmailList.xlsx')
worksheet = workbook.active

for row in worksheet.iter_rows(min_row=2):
    email_to = row[0].value
    print(email_to)

email_from_address = env('email_from_address')
email_password = env('email_password')
host = "smtp.gmail.com"
port = '587'

server = smtplib.SMTP(host,port)
server.ehlo()
server.starttls()
server.login(email_from_address, email_password)


email_body = "<b>Teste email TLS em HTML negrito</b>"
email_msg = MIMEMultipart()
email_msg['From'] = email_from_address
email_msg['To'] = email_to
email_msg['Subject'] = 'Teste TLS'
email_msg.attach(MIMEText(email_body, 'html')) 

to_send_file = 'C:\\Users\\joyce\\Inventory\\vendas_de_produtos.xlsx'
attachment = open(to_send_file, 'rb') 

att = MIMEBase('application', 'octet-stream') 
att.set_payload(attachment.read()) 
encoders.encode_base64(att) 

att.add_header('Content-Disposition', f'attachment; filename = vendas_de_produtos.xlsx')
attachment.close()
email_msg.attach(att)

server.sendmail(email_msg['From'],email_msg['To'], email_msg.as_string())
server.quit()



