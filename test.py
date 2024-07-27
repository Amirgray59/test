import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

model = LinearRegression()
df = sns.load_dataset("iris")

data = []

for i in df :
  data.append(df[i])

x = df.iloc[:, :-1]
y = df.iloc[:, -1]

for i in df :
    enc = LabelEncoder()
    enc.fit(df[i])
    df[i] = enc.transform(df[i])
