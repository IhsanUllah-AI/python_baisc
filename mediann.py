import pandas as pd
import numpy as np
df=pd.read_csv("med.csv")
print(df)
#in this data set we have outlier (data point in data set  very very differnet from other data points) elon
#we have miss value for laiba now we guess this value to fill it  if i take avg there is elon(showroom example(stat analysis full data set) also missing value(data cleaining)) 
print("avg of data",df['monthly income'].mean()) #very large bcs of outlier
#so in this case i will take the middle value find 
stat=df.describe()
print(stat) #show basic stat 
#quantile find any percentage 
md=df['monthly income'].quantile(0.5) #to find middle
print("median=",md)
md=df['monthly income'].quantile(0.75) #to find 75
print("75=",md)
md=df['monthly income'].quantile(0.25,interpolation='lower')#to find 25% "lower "will take to lower index if  25% exist middl bet two value  higher will take to high
print("25=",md)
med=df['monthly income'].median()
print("median",med)
df=df.fillna(df['monthly income'].median()) #fill missing value with median value 
print(df)
df.to_csv('med.csv',index=False) #save changes in dataset

#no i form  csv dataset to remove outlier from it
df_new=pd.DataFrame({
    'name':["shehzad","waqas","Att ullah","ali","ihsan","waqar","Adeeba","laiba","mahi","aslam channa","channa","aslam","A","A","A","A","A","A","A","A",],
    'height':[1.2,2.3,4.9,5.1,5.2,5.4,5.5,5.5,5.6,5.6,5.8,5.9,6,6.1,6.2,6.5,7.1,14.5,23.2,40.2]
})
df_new.to_csv('height.csv',index=False)
st=df_new.describe() #find all statistcs  25% which is q1 also we calculate using quantile
print("statistics of height=",st)
q1=df_new['height'].quantile(0.25) #find  25%
q3=df_new['height'].quantile(0.75) #find 75% all these are calculted in describe but here cal separly
iqr=q3-q1
#find lower whisker and upper all those value not occur in this range will be outlier
lower_limit=(q1-1.5*iqr).__round__(2)
upper_limit=(q3+1.5*iqr).__round__(2)
print("lower limit=",lower_limit)
print("upper limit=",upper_limit)
outlier=df_new[(df_new["height"]<lower_limit) | (df_new["height"]>upper_limit)] #find outlies
print("outlier")
print(outlier)
#now make new datset to remove outlier from it
df_no_outlier=df_new[(df_new["height"]>lower_limit) & (df_new["height"]<upper_limit)]
df_no_outlier.to_csv('height_no_outlier.csv',index=False)
  
