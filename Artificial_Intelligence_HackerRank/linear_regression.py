import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

CSV_COLUMNS = ["feature","label"]
a = pd.read_csv("data1.csv",delimiter=",",header=None)
a.columns = CSV_COLUMNS

x = np.array(a.drop(['label'],1))
y = np.array(a['label'])

plt.scatter(x,y)
plt.show()
x = preprocessing.scale(x)
regr = LinearRegression()

regr.fit(x, y)
print(regr.predict(int(input()))[0])
