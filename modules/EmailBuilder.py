import os
import environ
import smtplib
import openpyxl
import modules.SetLog
from GetRootDirectory import GetRootDirectory
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



class EmailSender:
    def __init__(self):
        env = environ.Env()
        env.read_env()
        self.email_from_address = env('email_from_address')
        self.email_password = env('email_password')
        self.host = 'smtp.gmail.com'
        self.port = '587'
        self.excel_file_path = 'ParametersFiles\\EmailList.xlsx'
        self.email_addresses = self.load_email_addresses_from_excel()
        self.set_log = modules.SetLog.SetLog()


    def load_email_addresses_from_excel(self):
        try:
            workbook = openpyxl.load_workbook(self.excel_file_path)
            worksheet = workbook.active
            email_addresses = []
            for row in worksheet.iter_rows(min_row=2):
                email_address = row[0].value
                email_addresses.append(email_address)
            return email_addresses
        except Exception as e:
            self.set_log.set_log_error(e)
            return []

    def configure_smtp_server(self):
        try:
            server = smtplib.SMTP(self.host, self.port)
            server.ehlo()
            server.starttls()
            server.login(self.email_from_address, self.email_password)
            return server
        except Exception as e:
            self.set_log.set_log_error(e)
            return None

    def create_email_message(self, notify, code='', email_body='Unexpected error'):
        if notify == 'Final':
            subject = 'FINAL'
            email_body = 'Process has finished'
        elif notify == 'SUCCESS':
            subject = 'SUCCESS REGISTRATION'
            email_body = f'Product {code} successfully registered'
        elif notify == 'REGISTRATION ERROR':
            subject = 'REGISTRATION ERROR'
            email_body = f'An error has occurred. Unable to register product {code}'
        elif notify == 'SCRIPT CRASH':
            subject = 'ScriptCrash'
            email_body = email_body
        else:
            subject = 'ERROR'
            email_body = f'Unexpected error has occur, unable to finish the process. Details: {email_body}'
        return subject, email_body

    def send_email(self, server, email_to, subject, email_body, attachments_file_path, notify):
        try:
            email_msg = MIMEMultipart()
            email_msg['From'] = self.email_from_address
            email_msg['To'] = email_to
            email_msg['Subject'] = subject
            email_msg.attach(MIMEText(email_body, 'html'))

            if notify == 'Final':
                for attachment_path in attachments_file_path:
                    attachment = open(attachment_path, 'rb')
                    att = MIMEBase('application', 'octet-stream')
                    att.set_payload(attachment.read())
                    encoders.encode_base64(att)
                    att.add_header('Content-Disposition', f'attachment; filename = {os.path.basename(attachment_path)}')
                    attachment.close()
                    email_msg.attach(att)

            server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
        except Exception as e:
            self.set_log.set_log_error(e)

    def main_email(self, notify, code='', email_body='', file_name=''):

        try: 
            get_root_directory = GetRootDirectory()
            root_directory = get_root_directory.GetDirectory()
            self.email_addresses = self.load_email_addresses_from_excel()
            


            if not self.email_addresses:
                self.set_log.set_log_error('No email adresses found')
                return

            server = self.configure_smtp_server()

            if server:
                subject, email_body = self.create_email_message(notify, code, email_body)
                attachments_file_path = [f'{root_directory}\\{file_name}', f'{root_directory}\\LOG.txt']

                for email_to in self.email_addresses:
                    self.send_email(server, email_to, subject, email_body, attachments_file_path, notify)

                server.quit()
        except Exception as e:
            self.set_log.set_log_error(e)
