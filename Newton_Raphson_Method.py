x=2
for i in range(100):
    xnew=x-(x**5-24)/(5*x**4)
    if abs(xnew-x)<0.00000001: break
    x=xnew

    
print(" the root is",x," at ",i,"iteration")
