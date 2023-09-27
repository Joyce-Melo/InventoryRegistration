import gdown, sys
import environ


def download_folders():
  #Enable systems environment
  env = environ.Env()
  environ.Env().read_env()

  #Downloading input folder
  input_folder_url = env('input_folder_url')
  parameters_folder_url = env('parameters_folder_url')
  outuput_folder = 'ParametersFiles'
  #url = sys.argv[1]
  if input_folder_url.split('/')[-1] == '?usp=sharing':
    input_folder_url= input_folder_url.replace('?usp=sharing','')
    
  gdown.download_folder(input_folder_url, output=outuput_folder)

  if parameters_folder_url.split('/')[-1] == '?usp=sharing':
    parameters_folder_url= parameters_folder_url.replace('?usp=sharing','')
    
  gdown.download_folder(parameters_folder_url, output=outuput_folder)

download_folders()

