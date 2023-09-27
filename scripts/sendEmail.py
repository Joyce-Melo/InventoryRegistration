import os
import environ
import smtplib
from email.message import EmailMessage
# from bot import code
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#Norma -> Padrão/Norma de envio de mensagem
# Imports para enviarmos anexo
from email.mime.base import MIMEBase
from email import encoders # Tranforma o arquivo em binário para poder fazer o envio
import openpyxl

#SMTP -> Servidor

env = environ.Env()
environ.Env().read_env()

#Get email from email list
workbook = openpyxl.load_workbook('ParametersFiles\\EmailList.xlsx')
worksheet = workbook.active

for row in worksheet.iter_rows(min_row=2):
    email_to = row[0].value
    print(email_to)


#Configurar email, senha
email_from_address = env('email_from_address')
email_password = env('email_password')
host = "smtp.gmail.com"
port = '587'
#Definir mensagens. Se sucesso for igual a True teremos uma mensagem de sucesso, se igual false, teremos a de erro
#Criar uma função para definição da mensagem, essa função recebe o código do produto, defini se foi sucesso ou não, cria a mensagem (sucesso e erro) e retorna a mensagem


server = smtplib.SMTP(host,port)
#Estamos usando um tipo de envio chamado TLS, que é uma camada de segurança a mais da google, por definição da google, para usarmos isso precisamos startat o TLS e fizemos isso chamando as funções ehlo e starttls (isso você encontra nas configs do gmail)

server.ehlo()
server.starttls()
server.login(email_from_address, email_password)


email_body = "<b>Teste email TLS em HTML negrito</b>"

email_msg = MIMEMultipart()
email_msg['From'] = email_from_address
email_msg['To'] = email_to
email_msg['Subject'] = 'Teste TLS'
email_msg.attach(MIMEText(email_body, 'html')) #Estou enviando o email do tipo plain, comum, aqui podemos mudar para HTML

#anexando arquivo
#Abrimos o arquivo em modo leitura e binary
to_send_file = 'C:\\Users\\joyce\\Inventory\\vendas_de_produtos.xlsx'
attachment = open(to_send_file, 'rb') #rb -> read binary

#Lemos o arquivo no modo binario e jogamos codificado em base 64 (que é o que o e-mail precisa)
att = MIMEBase('application', 'octet-stream') #Declarando um anexo do tipo binário mimebase
att.set_payload(attachment.read()) #lendo esse binário
encoders.encode_base64(att) #Codificando esse attachment em base64

#Adicionamos o cabeçalho no tipo anexo de email
att.add_header('Content-Disposition', f'attachment; filename = vendas_de_produtos.xlsx')
#fechamos o arquivo
attachment.close()
#colocamos o anexo no corpo do e-mail
email_msg.attach(att)


#Enviando mensagem
server.sendmail(email_msg['From'],email_msg['To'], email_msg.as_string())
server.quit()


