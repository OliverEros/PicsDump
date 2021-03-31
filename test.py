from package.folderparser import folderScraper
from package.fileScraper import Filescraper


t  = folderScraper()
f = Filescraper("/home/oliver/PicsDump/test/regular")

f.parseText(f.file)

t.searchFolder("/home/oliver")

