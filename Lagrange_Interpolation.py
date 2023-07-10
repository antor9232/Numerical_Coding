import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(a,f,x):
    yp=0
    
    assert a.size==f.size
    n=a.size
    
    for i in range(n):
        p=1
        for j in range(n):
            if i==j: continue
            p=p*(x-a[j])/(a[i]-a[j])
        yp=yp+p*f[i]
    return yp

#plot
a=np.linspace(0,np.pi*0.5,4)
f=np.sin(a)
x = np.linspace(-0.1*np.pi,0.6*np.pi,200)
y = lagrange_interpolation(a,f,x)
plt.plot(x,y,linestyle="--",label="Lagrange Interpolation")
plt.plot(x,np.sin(x),label="$\sin(x)$")
plt.scatter(a,f,c="black",label="Data Points")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc="best")
plt.show()

