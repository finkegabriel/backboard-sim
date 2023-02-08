import pandas as pd
import os

def readCsv(csvFile,delim):
    df = pd.read_csv(csvFile,delimiter=delim)
    return df

def outputCsv(d):
    dateFrame = pd.DataFrame(d,index=[0])
    dateFrame.to_csv("3d_bounce_traj.csv", mode='a',header=False,index=False)
    print("written out")