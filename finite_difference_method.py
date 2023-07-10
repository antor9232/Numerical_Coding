import numpy as np

f= lambda x: 0.1*x**5-0.2*x**3+0.1*x-0.2
h=0.001

df1=0.09405
df2=-0.118
def FDF(x):
    dff1= (f(x+h)-f(x))/h
    dff2= (f(x+2*h)-2*f(x+h)+f(x))/h**2
    print("FDF\t",dff1,"\t",dff1-df1,"\t",dff2,"\t",dff2-df2)
def BDF(x):
    dff1= (f(x)-f(x-h))/h
    dff2= (f(x)-2*f(x-h)+f(x-2*h))/h**2
    print("BDF\t",dff1,"\t",dff1-df1,"\t",dff2,"\t",dff2-df2)
def CDF(x):
    dff1= (f(x+h)-f(x-h))/(2*h)
    dff2= (f(x+h)-2*f(x)+f(x-h))/h**2
    print("CDF\t",dff1,"\t",dff1-df1,"\t",dff2,"\t",dff2-df2)

print("\t f'(x)\t\t\t  err\t\t\t          f''(x)\t\t\t err")
FDF(0.1)
BDF(0.1)
CDF(0.1)

