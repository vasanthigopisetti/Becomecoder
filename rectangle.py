from math import*
l,b=map(float,input().split())
area=l*b
per=2*(l+b)
dia=sqrt(l**2+b**2)
print("%.2f"%dia,end="")
