import platform
# Both Linux and Windows different slashes.
# Used for detecting the sys and apply the appropriate slash type
class Configuration:
    def __init__(self):
        self.OS = None
        self.slash = None


    def which_OS(self):
        plt = platform.system()

        if plt == 'Windows':
            self.slash = '\\'
            self.OS = "Windows"
        elif plt == 'Linux' or plt == 'Darwin':
            self.OS = 'Linux' if plt == 'Linux' else 'Darwin'
            self.slash = '/'



