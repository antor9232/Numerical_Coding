def rfalsi(f,a,b,tol,maxi):
    x=0
    i=1
    if f(a)*f(b)<0:
        for i in range(maxi):
            x=((a*f(b)-b*f(a))/(f(b)-f(a)))
            if abs(x-a)<tol : break
            elif f(a)*f(b)<0:
                b=x
            else:
                a=x
        else:
            print("No roots within the range")

        return x,i
y=lambda x: x**2-5*x+6

#a=float(input("ENter a: "))
#b=float(input("ENter b: "))

r,n=rfalsi(y,1,2,0.001,4)
print("the root is: ",r,"at",n," iteration")
