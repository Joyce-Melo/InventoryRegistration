from GetRootDirectory import GetRootDirectory
from modules.SetLog import SetLog
from modules.DownloadFiles import DownloadFiles
from modules.SetFileNameAndPath import SetFileNameAndPath
from modules.ProductRegistration import ProductRegistration
from modules.EndProcess import EndProcess
from modules.UploadFiles import UploadFiles
from modules.EmailBuilder import EmailSender


class Main:
    def __init__(self):

            try: 
                SetLog()
                root_directory = GetRootDirectory().GetDirectory()

                download_files = DownloadFiles()
                download_files.input_folder_download()
                download_files.parameters_folder_download()
 
                get_file_name_and_path = SetFileNameAndPath()
                file_name_and_path, data_frame = get_file_name_and_path.set_file_name_to_work_with()
                
                product_registration = ProductRegistration()
                product_registration.register_product(data_frame=data_frame, file_name=file_name_and_path)
                new_wrokbook_name = product_registration.new_file_name

                upload_function = UploadFiles()
                upload_function.upload_file(f"{root_directory}\\LOG.txt")
                upload_function.upload_file(f"{root_directory}\\{new_wrokbook_name}")
              
                EndProcess().clear_process()

            except Exception as e:
                email_builder = EmailSender()
                email_builder.main_email(notify='SCRIPT CRASH', email_body=e)
                EndProcess().clear_process()
Main()

        


