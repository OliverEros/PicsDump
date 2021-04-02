import re
import codecs
from .folderparser import *

class Filescraper:
    def __init__(self, file = ""):
        self.file = file
        self.regex = '[\w]*\.jpg|[\w]*\.png|[\w]*\.GIF|[\w]*\.gif'
        self.foundImages = {}

    def parseText(self, path):
        if(folderScraper.pathExists(path)):
            file = codecs.open(folderScraper.formatText(path)  + "index.html", "r", "utf-8").read()
            formated = re.sub('\s*', '',file, count=0)
            self.foundImages  = {i for i in re.findall(re.compile(self.regex),formated)}

    def print_images(self):
        print(self.foundImages)
                    
            

    
