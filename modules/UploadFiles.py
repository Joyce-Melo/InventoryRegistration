import datetime
import os
from datetime import date
from googleapiclient.discovery import build
from google.oauth2 import service_account
from GetRootDirectory import GetRootDirectory
from modules.EmailBuilder import EmailSender

class UploadFiles:


        def __init__(self):
            get_root_directory = GetRootDirectory()
            root_directory = get_root_directory.GetDirectory()
            self.SCOPES = ['https://www.googleapis.com/auth/drive']
            self.SERVICE_ACCOUNT_FILE = f'{root_directory}\\modules\\service_account.json'
            self.LOG_PARENT_FOLDER_ID = '1IYHQTwdCDXQqClUJdL5y0xcG5knXnrPi'
            self.INVENTORY_PARENT_FOLDER_ID = '18dI8qFLtsws2ApfWqhccqZdlufWNEB2G'

        def authenticate(self):
            creds = service_account.Credentials.from_service_account_file(self.SERVICE_ACCOUNT_FILE, scopes=self.SCOPES)
            return creds

        def upload_file(self, file_path):
            try:
                creds = self.authenticate()
                service = build('drive', 'v3', credentials=creds)
                today = date.today() 
                date_formatted = '{}.{}.{}'.format(today.day, today.month, today.year)

                if 'LOG' in file_path:
                    name = 'LOG - '+date_formatted
                    parent = [self.LOG_PARENT_FOLDER_ID]


                elif 'Inventory' in file_path:
                    name = os.path.basename(file_path)
                    parent = [self.INVENTORY_PARENT_FOLDER_ID]

                file_metadata = {
                'name' : name,
                'parents' : parent
                }

                file = service.files().create(
                body=file_metadata,
                media_body=file_path
                ).execute()
            except Exception as e:
                email_builder = EmailSender()
                email_builder.main_email(notify='SCRIPT CRASH', email_body=e)
                print(e)




                