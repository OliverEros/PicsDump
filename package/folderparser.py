import os


class folderScraper:
    def __init__(self, path=""):
        self.extensions = ['.jpg', '.gif', '.GIF', '.txt', '.png']
        self.path = path
        self.images = {}

    def searchFolder(self, path):
        if not folderScraper.pathExists(path):
            raise Exception("Path " + path + " does not exist!")
        else:  
            self.path = folderScraper.formatText(path)
            self.images = {f for f in os.listdir(self.path + '/images') if os.path.isfile(self.path + "/images/" + f) and self.getPicturesOnly(f) == True}

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

    @staticmethod
    def formatText(path):
        if path[-1] != "/":
            return path + "/"
        else:
            return path
    
    @staticmethod
    def pathExists(path):
        if os.path.exists(path):
            return True
        else:
            return False
