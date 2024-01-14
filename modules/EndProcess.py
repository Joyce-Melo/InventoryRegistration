import os
from GetRootDirectory import GetRootDirectory
import shutil
import modules.SetLog

class EndProcess:
    def __init__(self):
        get_root_directory = GetRootDirectory()
        root_directory = get_root_directory.GetDirectory()
        self.logging = modules.SetLog.SetLog()
        self.directory_folder_to_remove = f'{root_directory}\\ParametersFiles'
        self.log_path_to_remove = f'{root_directory}\\LOG.txt'

    def clear_process(self):
        try:
            shutil.rmtree(self.directory_folder_to_remove)
        except OSError as e:
            print(f'Unable to delete ParametersFiles folder. Details: {str(e)}')

        try:
            self.logging.close_log()
            os.remove(self.log_path_to_remove)
        except OSError as e:
            print(f'Unable to delete Log File. Details: {str(e)}')
