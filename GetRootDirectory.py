import os

class GetRootDirectory:

    def __init__(self):
        pass

    def GetDirectory(self):
        root_directory = os.getcwd()
        return root_directory