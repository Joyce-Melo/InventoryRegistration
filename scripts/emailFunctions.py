import os
import environ
import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import openpyxl

def load_email_addresses_from_excel(file_path):
    try:
        workbook = openpyxl.load_workbook(file_path)
        worksheet = workbook.active
        email_addresses = []
        for row in worksheet.iter_rows(min_row=2):
            email_address = row[0].value
            email_addresses.append(email_address)
        return email_addresses
    except Exception as e:
        print(f"Erro ao carregar os endereços de e-mail do arquivo Excel: {str(e)}")
        return []

def configure_smtp_server(host, port, email_from_address, email_password):
    try:
        server = smtplib.SMTP(host, port)
        server.ehlo()
        server.starttls()
        server.login(email_from_address, email_password)
        return server
    except Exception as e:
        print(f"Erro ao configurar o servidor SMTP: {str(e)}")
        return None
    
def create_email_message(success, code):
     
    if success == 'Final':
        subject = "FINAL"
        email_body = "Process has finished"
    elif success:
        subject = "SUCCESS REGISTRATION"
        email_body = "Product "+ code +  " successfully registered"
    elif success == 'SCRIPT CRASH':
        subject = "ScriptCrash"
        email_body = "Unexpected error, unable to finish process"
    else:
        subject = "REGISTRATION ERROR"
        email_body = "An error has occurred. Unable to register product " + code
    return subject, email_body


        
def send_email(server, email_from_address, email_to, subject, email_body, attachment_file_path,sucess):
    try:
        email_msg = MIMEMultipart()
        email_msg['From'] = email_from_address
        email_msg['To'] = email_to
        email_msg['Subject'] = subject
        email_msg.attach(MIMEText(email_body, 'html'))

        if sucess == 'Final':
            attachment = open(attachment_file_path, 'rb')
            att = MIMEBase('application', 'octet-stream')
            att.set_payload(attachment.read())
            encoders.encode_base64(att)
            att.add_header('Content-Disposition', f'attachment; filename = {os.path.basename(attachment_file_path)}')
            attachment.close()
            email_msg.attach(att)
        
        server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
        print(f"E-mail enviado para {email_to}")
    except Exception as e:
        print(f"Erro ao enviar o e-mail para {email_to}: {str(e)}")

def main_email(success, code):
    env = environ.Env()
    environ.Env().read_env()

    email_from_address = env('email_from_address')
    email_password = env('email_password')
    host = "smtp.gmail.com"
    port = '587'

    excel_file_path = 'ParametersFiles\\EmailList.xlsx'
    email_addresses = load_email_addresses_from_excel(excel_file_path)

    if not email_addresses:
        print("Nenhum endereço de e-mail encontrado no arquivo Excel.")
        return

    server = configure_smtp_server(host, port, email_from_address, email_password)

    if server:
        # email_body = "<b>Teste de e-mail TLS em HTML em negrito</b>"
        # subject = 'Teste TLS'
        subject, email_body = create_email_message(success, code)
        attachment_file_path = 'C:\\Users\\joyce\\Inventory\\ParametersFiles\\products_inventory-28.8.2023 - Completed.xlsx'

        for email_to in email_addresses:
            send_email(server, email_from_address, email_to, subject, email_body, attachment_file_path,success)

        server.quit()
    else:
        print("Falha ao configurar o servidor SMTP.")

if __name__ == "__main__":
    main_email()
