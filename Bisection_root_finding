def bisection(f,a,b,tol,maximum):
    for i in range(maximum):
        c=(a+b)/2
        if abs(a-c)<tol:
            break
        else:
            if f(a)*f(c)<0:
                b=c
            else:
                a=c
    return c,i
    
y= lambda x: x**5-24
r,n=bisection(y,1,2,0.0001,100)
print(r,"is the root at ",n," iteration")

                 
