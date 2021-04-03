import re
import codecs

from package.utils import format_path,file_exists

class Filescraper:
    def __init__(self,OS, file = ""):
        self.file = file
        self.regex = '[\w]*\.jpg|[\w]*\.png|[\w]*\.GIF|[\w]*\.gif'
        self.foundImages = {}
        self.slash = r"{}".format(OS)

    def parseText(self, path):
            file =format_path(path,self.slash,0)
            print(file)
            if file_exists(file):
                file = codecs.open(file, "r", "utf-8").read()
                formated = re.sub('\s*', '',file, count=0)
                self.foundImages  = {i for i in re.findall(re.compile(self.regex),formated)}
            else:
                raise Exception("No html file was found")


    def print_images(self):
        print(self.foundImages)
    
                    
            

    
