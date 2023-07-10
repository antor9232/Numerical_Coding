
def secant(fn,x1,x2,tol,maximum):
    for i in range(maximum):
       xnew=x2-((x2-x1)/(fn(x2)-fn(x1))*fn(x2))
       if abs(xnew-x2)<tol: break
       else:
          x1=x2
          x2=xnew
    return xnew,i

f= lambda x: x**4+3*x**3+6*x**2-8

x1=float(input("enter x1: "))
x2=float(input("enter x2: "))
tol=float(input("enter tol: "))
x,n=secant(f,x1,x2,tol,100)
print("the root is ",x,"at",n," iteration")     
