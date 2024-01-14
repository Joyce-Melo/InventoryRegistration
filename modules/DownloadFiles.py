import gdown
import environ
# import modules.SetLog

class DownloadFiles:
    def __init__(self):
            env = environ.Env()
            env.read_env()
            self.input_folder_url = env('input_folder_url')
            self.parameters_folder_url = env('parameters_folder_url')
            self.output_folder = 'ParametersFiles'
            # self.set_log = modules.SetLog.SetLog()

    def input_folder_download(self):
        try:
            if self.input_folder_url.split('/')[-1] == '?usp=sharing':
                self.input_folder_url = self.input_folder_url.replace('?usp=sharing','')
            gdown.download_folder(self.input_folder_url, output=self.output_folder)
            # self.set_log.set_log_info('Input folder downloaded succesfully')
            
        except Exception as e:
            # self.set_log.set_log_error(str(e))
            print(e)

    def parameters_folder_download(self):
        try:
            if self.parameters_folder_url.split('/')[-1] == '?usp=sharing':
                self.parameters_folder_url = self.parameters_folder_url.replace('?usp=sharing','')
            gdown.download_folder(self.parameters_folder_url, output=self.output_folder)
            # self.set_log.set_log_info('Parameter folder downloaded succesfully')

        except Exception as e:
            # self.set_log.set_log_error(str(e))
            print(e)

download = DownloadFiles()
download.input_folder_download()
download.parameters_folder_download()

