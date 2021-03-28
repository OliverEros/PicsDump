from package.fileScraper import Filescraper
from package.folderparser import folderScraper

import os
import sys

# Prompts user for folder path
def get_path():
   return input('Enter path: ')

# Checks if there is a need to delete images at all
# by comparing the two sets of found image names
def should_delete(set1, set2):
    if set1 == set2:
        return False
    else:
        return True

# Compares sets and deletes images that are not present in both 
# If variable 'will_delete' is True, delete, otherwise prints image names only!
def delete_pictures(path, set1, set2, will_delete):
    to_recurs = False

    for a in set1.copy():
        for b in set2.copy():
            if a == b:
                set1.remove(a)
                set2.remove(b)
    if will_delete:
        [print(name + ' deleted!') for name in set1] + [os.remove(path + 'images/' + file) for file in set1]
    else:
        [print(name + ' unused!') for name in set1]

# Start of program
def start():
    # Instead of deleting images, only prints their name
    to_delete = True
    if '-s' in sys.argv:
        to_delete = False


    foparser = folderScraper()
    fiparser = Filescraper()


    path = get_path()
    print(path)

    try:
         foparser.searchFolder(path)  
    except Exception as e:
        print(e)
        start()
    else:
        foparser.searchFolder(path)
        fiparser.parseText(path)

         # Check if images need to be deleted
        if not should_delete(foparser.images, fiparser.foundImages):
            print('No unused image was found')
        else:
            delete_pictures(path, foparser.images, fiparser.foundImages, to_delete)


if __name__ == '__main__':
    start()







