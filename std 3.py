#how far a part a individual  data point from average or how data spread with respect to average 
#we have data set of 6 sample which is java score
import pandas as pd
import numpy as np
df=pd.DataFrame({
    'name':['ihsan','Atiq','farhana','adeeba','huzaifa','jafar'],
    'marks':[90,45,96,87,96,82]
}
)
print(df)
avg=df['marks'].mean().__round__(2)
print("average=",avg)
import matplotlib.pyplot as plt
plt.scatter(df['marks'],df['name'],color='b')# x and y must be of same size
plt.scatter([avg],[0],color='r')
plt.xlabel('MARKS')
plt.title("MARKS & AVERAGE")
plt.legend()
plt.yticks([]) #hide y
plt.grid(True)
plt.show()
#we find that how much value is far away than average for each individual
diff= (df['marks']-avg).abs()
print("differince",diff)
#take mean of diff which is called mean absolute deviation
mad=diff.mean()
print("Mean Absolute deviation =",mad) #high mad vale mean value more widely spreed from avg 
#mad not give more information bcs let we have a two dataset which is same mad value  but one is high spreeding value how we can say which is more std
#we used standard devition for this case in which we square the diff value then take avg of it and then under root which is come differnet alway
#more std value mean data widely spreed from avg
sq=diff*diff #will squre diff value 
av=sq.mean() #take avg of it
import math 
ur=math.sqrt(av)
print("standard deviation=",ur) 

