N=[eval(x) for x in input("enter the elements of list seperated by comma").split(",")]
print(N)
N.sort()
N.reverse()
mul=1
for i in N[0:3]:
    mul*=i
print("max multiply of the list elments using three elements is:",mul)    
        
