import subprocess
import sys
import glob

from os import listdir, getcwd
from os.path import isfile, join, basename


# Gets files at path
def getScripts(path: str) -> list:
    return [basename(x) for x in glob.glob(getcwd() + path + "/*.py")]

def process(xlName: str, scriptName: str) -> bool:
    pExec = sys.executable
    scriptPath = getcwd() + "/transformation/scripts/" + scriptName
    xlPath = getcwd() + "/uploadedFiles/" + xlName

    result = subprocess.run([pExec, scriptPath, xlPath])

    if result.returncode == 0:
        return True
    else:
        return False