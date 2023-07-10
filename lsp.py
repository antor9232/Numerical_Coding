import numpy as np
def LeastSqPoly(x1,x2,x3,y1,y2,y3):
    x=np.array([[1,x1,x1**2],[1,x2,x2**2],[1,x3,x3**2]])
    y=np.array([y1,y2,y3])
    c=x.transpose().dot(x)
    d=np.linalg.inv(c)
    e=d.dot(x.transpose())
    a=e.dot(y)
    return a
print(LeastSqPoly(1,2,3,2,4,6))

    
