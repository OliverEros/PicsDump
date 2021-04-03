import os
"""
Function to format path depending on requirements.
Takes argument 'fi_fo' (file (0) or folder (1))
"""
def format_path(path,slash,fi_fo):

    
    path = r"{}".format(path)

    if path[-1] != slash:
        if fi_fo == 0:
            return path + slash + "index.html"
        else:
            return path + slash + "images" + slash
    else:
        if fi_fo == 0:
            return path + "index.html"
        else:
            return path + "images" + slash

"""
Checks if a given path exists
"""
def path_exists(path):
    if os.path.exists(path):
        return True
    else:
        return False

"""
Checks if a given file exists
"""
def file_exists(filepath):
    if os.path.isfile(filepath):
        return True
    else:
        return False
