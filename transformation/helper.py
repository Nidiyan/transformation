from os import listdir, getcwd
from os.path import isfile, join

# Gets files at path
def getScripts(path: str) -> list:
    return [f for f in listdir(getcwd() + path) if isfile(join(getcwd() + path, f))]