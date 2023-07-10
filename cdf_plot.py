import numpy as np
import matplotlib.pyplot as plt
f= lambda x: 0.1*x**5-0.2*x**3+0.1*x-0.2
f1= lambda x: 0.5*x**4-0.6*x**2+0.1
f2= lambda x: 2*x**3-1.2*x
h=0.2

df1=0.09405
df2=-0.118
x = np.linspace(-10,10)
#central Difference formula
dff1= (f(x+h)-f(x-h))/(2*h)
dff2= (f(x+h)-2*f(x)+f(x-h))/h**2
   

#plot
plt.plot(x,f(x),linestyle="--",label="f(x)")
plt.plot(x,f1(x)-dff1,linestyle="--",label="f1E(x)")
plt.plot(x,dff1,linestyle="-.",label="f'(x)")
plt.plot(x,f2(x)-dff2,linestyle="--",label="f2E(x)")
plt.plot(x,dff2,linestyle="-",label="f''(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["f(x)","f1(x)","f'(x)","f2(x)","f''(x)"])
plt.grid()
plt.show()
