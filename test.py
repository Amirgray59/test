import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

model = LinearRegression()
df = sns.load_dataset("iris")

x = 1
y = []

data = []

for i in df :
  data.append(df[i])
print(data)
