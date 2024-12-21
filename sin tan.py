#a forest officer find height of tree  which is away from him 50 feet and they at top make angle with them is 30 degree 
#find height (height is perpindicular side and 50 feet is base )
#we kmow tan(teta)=p/b
import math
teta=30
b=50
#360=2pi 
ang=(teta*2*math.pi)/360 #conert 30 to rad
a=math.tan(ang) #return radian value and take radian value as well
height=(a*b).__round__(2)
print("height of tree=",height)

#we full some thing apply force of 10 Newton which is two axis x axis and y axis make ang of 30 degree
#find x aixs we know cost=base/hypo  and sint=per/hyp
hyp=10
x=(hyp*math.cos(ang)).__round__(2)
print("x axis froce =",x)
y=(hyp*math.sin(ang)).__round__(2)
print("y axis froce =",y)