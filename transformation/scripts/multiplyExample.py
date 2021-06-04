import pandas as pd 
import numpy as np 
import argparse
 
import os
 
# NOTE: FIGURE OUT HOW TO SAVE IN THE PROPER LOCATION -> SHOULD BE SAVED TO /GENERATED FILES
# CAN PASS COMPLETE PATH TO BOTH INPUT AND OUTPUT XL FILE
 
parser = argparse.ArgumentParser()
parser.add_argument('pathToFile', help='Path to File')
parser.add_argument('fileName', help='Name of File')
args = parser.parse_args()
pathToFile = args.pathToFile
fileName = args.fileName
 
fullPath = os.path.join(pathToFile,'uploadedFiles',fileName)
fullPathDownload = os.path.join(pathToFile,'generatedFiles', 'Output-' + fileName)
 
df = pd.read_excel(fullPath, engine='openpyxl')
 
df['product'] = df['num1'] * df['num2']
 
df.to_excel(fullPathDownload, index=False)
