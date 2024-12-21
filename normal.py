#normal distribution or gaussain distribution
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.DataFrame({
    'name':['A','B','C','D','E','F','G','H','I'],
    'height':[6.2,5.7,4.6,5.4,5.9,4.3,5.1,5.2,4.9]
})
plt.hist(x=df['height'],edgecolor='r', bins=5) #y axis sample how muc sample exist in this range 
plt.show()
#bell curve or gussain curve 
#N_dis used for remove outlier 
#how find outlier :bell curve middle poin called avg on rhs is +ive std left side minus std
#68.3%  data point fall uder plus minus one std range 95.5%  plus minus 2 97.7%  plus minus 3 std range outof three 3 is outlier found 
#by mathmetsicin and statiscian by apply many n_d test on data set
dff=pd.read_csv('heigh.csv')
stat=dff['Height(Inches)'].describe()
print("stat of height")
print(stat)
#now is use seaborn to plot cure with hist using histplot function
import seaborn as sns
sns.histplot(dff['Height(Inches)'],kde=True)#kde draw bell curve false not draw
plt.show()
# now remove outlier from it
avg=dff['Height(Inches)'].mean()
print("mean=",avg)
stdd=dff['Height(Inches)'].std()
print("std=",stdd)
#we now plus and minus 3 behind is outlier 
l_limi=avg-3*stdd
u_limit=avg+3*stdd
print('lower limit=',l_limi)
print('upper limit=',u_limit)
outlier=dff[(dff['Height(Inches)']<l_limi)|(dff['Height(Inches)']>u_limit)]
outlier.to_csv('heigh_with_outlier.csv',index=False)
print("outlier")
print(outlier.index(False))
dff_no_outlier=dff[(dff['Height(Inches)']>l_limi)&(dff['Height(Inches)']<u_limit)]
dff_no_outlier.to_csv('heigh_no_outlier.csv',index=False)
