def ackerman(m,n):
    if m==0:
        return n+1
    elif m!=0 and n==0:
        return ackerman(m-1,1)
    else:
        return ackerman(m-1,ackerman(m,n-1))

m=eval(input("enter the value of m:"))
n=eval(input("enter the value of n:"))
print("the result for ",m," and ",n," is:",ackerman(m,n))
