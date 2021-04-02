from package.fileScraper import Filescraper
from package.folderparser import folderScraper
from package.banner import banner
from configuration.configuration import Configuration
from colorama import Fore, Style

import subprocess
import os
import sys

# Prompts user for folder path
def get_path():
   return input('\n\nEnter path: ')

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
def start(error_message = None):
    
    #Safe mode. If 4 any reason images should not be deleted
    to_delete = True
    if '-s' in sys.argv:
        to_delete = False
   
    # Declaring objects
    os_detector = Configuration()
    os_detector.which_OS()

    foparser = folderScraper(os_detector.slash)
    fiparser = Filescraper()
    # Prints banner
    print(Fore.BLUE + banner + Style.RESET_ALL)

    #Prints error message if there is any, else pass
    if error_message == None:
        pass
    else:
        print(Fore.RED + str(error_message) + Style.RESET_ALL)
    
    #Get path from user
    path = get_path()
    print('Path is set to: ' + path)

    #Check for errors
    try:
         foparser.searchFolder(path)  
    except Exception as e:
#        subprocess.run('clear') 
        start(e)
    else:
        fiparser.parseText(path)

         # Check if images need to be deleted
        if not should_delete(foparser.images, fiparser.foundImages):
            print('No unused image was found')
        else:
            delete_pictures(path, foparser.images, fiparser.foundImages, to_delete)


if __name__ == '__main__':
    start()







