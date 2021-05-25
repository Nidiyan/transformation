import subprocess
import sys
import glob

from os import listdir, getcwd
from os.path import isfile, join, basename

initialPath = getcwd() + "/"

# Gets files at path
def getScripts(path: str) -> list:
    newPath = initialPath + path
    return [basename(x) for x in glob.glob(newPath + "/*.py")]

def process(xlName: str, scriptName: str) -> bool:
    pExec = sys.executable
    scriptPath = initialPath + "transformation/scripts/" + scriptName
    xlPath = initialPath + "uploadedFiles/" + xlName

    result = subprocess.run([pExec, scriptPath, xlPath])

    if result.returncode == 0:
        return True
    else:
        return False
