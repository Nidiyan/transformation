import pandas as pd 
import numpy as np 
import argparse

# NOTE: FIGURE OUT HOW TO SAVE IN THE PROPER LOCATION -> SHOULD BE SAVED TO /GENERATED FILES
# CAN PASS COMPLETE PATH TO BOTH INPUT AND OUTPUT XL FILE

initialPath = "/home/myawesomeproject/transformation/"

parser = argparse.ArgumentParser()
parser.add_argument('pathToFile', help='File to read in')
args = parser.parse_args()
pathToFile = args.pathToFile

df = pd.read_excel(pathToFile)

df['product'] = df['num1'] * df['num2']

df.to_excel(initialPath + '/generatedFiles/excelTestOutput.xlsx', index=False)