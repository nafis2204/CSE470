import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#preprocessing train set for primary models
dataset=pd.read_csv('bank.csv')
df=dataset
df=df.drop(["duration","job","contact","month","poutcome"],axis=1)

df["marital"] = [0 if each== "single" else 1 for each in df.marital]
df["default"] = [0 if each== "no" else 1 for each in df.default]
df["housing"] = [0 if each== "no" else 1 for each in df.housing]
df["loan"] = [0 if each== "no" else 1 for each in df.loan]
df["y"] = [0 if each== "no" else 1 for each in df.y]

print(df.columns)

