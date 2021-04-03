import os
from package.utils import format_path,path_exists,file_exists

class folderScraper:
    def __init__(self,OS, path=""):
        self.extensions = ['.jpg', '.gif', '.GIF', '.txt', '.png']
        self.path = path
        self.images = {}
        #Use appropriate slash (/ or \) depending on OS
        self.slash = r"{}".format(OS)

    def searchFolder(self, path):
        if not path_exists(path):
            raise Exception("Path " + path + " does not exist!")
        elif not path_exists(format_path(path,self.slash,1)):
            raise Exception("Path " + path + " has no image folder!")
        else:
            self.path = format_path(path, self.slash,1)
            self.images = {f for f in os.listdir(self.path) if file_exists(self.path + f) and self.getPicturesOnly(f) == True}

    def print_files(self):
       print(self.images)


    def getPicturesOnly(self, file):
        match = False

        for ext in self.extensions:
            if file[-4:] == ext:
                match = True
                break
            else:
                match = False

        return match

    def return_found(self):
        return self.images

   

