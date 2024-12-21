import pandas as pd
import numpy as np
df=pd.read_csv('heightweight.csv')
print(df.head()) #show first 5
print(df.tail()) #show last 5 give numb show that numb equal row
st=df['Weight(Pounds)'].describe()
print(st)
#find 25%
q1=df['Weight(Pounds)'].quantile(0.25)
q3=df['Weight(Pounds)'].quantile(0.75)
iqr=q3-q1
lower_limit=q1-1.5*iqr
upper_limit=q3+1.5*iqr
print("lower limit=",lower_limit)
print("upper limit=",upper_limit)
outlier=df[(df['Weight(Pounds)']<lower_limit)|(df['Weight(Pounds)']>upper_limit)]
print("outlier in weight")
print(outlier)
q1=df['Height(Inches)'].quantile(0.25)
q3=df['Height(Inches)'].quantile(0.75)
iqr=q3-q1
lower_limit=q1-1.5*iqr
upper_limit=q3+1.5*iqr
print("lower limit=",lower_limit)
print("upper limit=",upper_limit)
outlier=df[(df['Height(Inches)']<lower_limit)|(df['Height(Inches)']>upper_limit)]
print("outlier in Height")
print(outlier)
