import csv
import os
import pandas as pd

def readCsv(csvFile,delim):
    df = pd.read_csv(csvFile,delimiter=delim)
    return df
