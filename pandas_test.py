# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 21:20:01 2017

@author: jagan
"""

import pandas as pd
import matplotlib.pyplot as plt

file='C://Users//jagan//Desktop//Python Exercise//Salary_Data.csv'

dataset=pd.read_csv(file)

print(dataset)
X=dataset.iloc[:,0]
y=dataset.iloc[:,1]

plt.scatter(X,y)

dataset.describe()
dataset.head(3)
dataset.tail(3)

y.head(3)
X.iloc[20:26]
dataset.iloc[20:26,:]
dataset.iloc[0,:]
dataset.shape
dataset.info()
dataset.columns=['Years of Experience','Salary_1' ]
dataset.index=['S_no' ]

dataset.sort_values('Salary_1',ascending=False)
dataset.groupby('Salary_1')

#Statistics
dataset.describe()
dataset.mean()
dataset.corr()
dataset.max()
dataset.min()
dataset.median()
dataset.std()





