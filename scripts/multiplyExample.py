import pandas as pd 
import numpy as np 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('pathToFile', help='File to read in')
args = parser.parse_args()
pathToFile = args.pathToFile

df = pd.read_excel(pathToFile)

df['product'] = df['num1'] * df['num2']

df.to_excel('excelTestOutput.xlsx', index=False)