def nraphson(fn, dfn, x, tol, maxiter):
    for i in range(maxiter):
        xnew=x-fn(x)/dfn(x)
        if abs(xnew-x)<tol: break
        x=xnew
    return xnew,i

y= lambda x: x**5-24
dy= lambda x: 5*x**4

x,n = nraphson(y,dy,3,0.0001,1)
print("the root is",x, "at ",n," iteration")

"""

def nraphson(fn, x, tol, maxiter):
    for i in range(maxiter):
        xnew=x-fn[0](x)/fn[1](x)
        if abs(xnew-x)<tol: break
        x=xnew
    return xnew,i

y=[lambda x: x**5-24, lambda x: 5*x**4]

x,n = nraphson(y,2,0.0001,100)
print("the root is",x, "at ",n," iteration")"""
