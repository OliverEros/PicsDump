import os


class folderScraper:
    def __init__(self, path=""):
        self.extensions = ['.jpg', '.gif', '.GIF', '.txt', '.png']
        self.path = path
        self.images = {}

    def searchFolder(self, path):
        if not folderScraper.pathExists(path) or not folderScraper.pathExists(folderScraper.formatText(path)):
            raise Exception("Path " + path + " does not exist!")
        else:
            print('we got here, boys')
            self.path = folderScraper.formatText(path)
            self.images = {f for f in os.listdir(self.path) if os.path.isfile(self.path + f) and self.getPicturesOnly(f) == True}

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
            return path + "/images/"
        else:
            return path
    
    @staticmethod
    def pathExists(path):
        if os.path.exists(path):
            return True
        else:
            return False
