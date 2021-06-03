import subprocess
import sys
import glob

from os import listdir, getcwd
from os.path import isfile, join, basename

initialPath = getcwd() + "/"

# Gets files at path
def getScripts(path: str) -> list:
    return [basename(x) for x in glob.glob(path + "/*.py")]

def process(xlName: str, scriptName: str, path: str) -> bool:
    pExec = sys.executable
    scriptPath = path + "transformation/scripts/" + scriptName
    xlPath = path + "uploadedFiles/" + xlName

    result = subprocess.run([pExec, scriptPath, xlPath])

    if result.returncode == 0:
        return True
    else:
        return False