import pandas as pd
import os

def readCsv(csvFile,delim):
    df = pd.read_csv(csvFile,delimiter=delim)
    return df
