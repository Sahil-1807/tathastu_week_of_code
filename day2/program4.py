for i in range(5,0,-1):
    for j in range(i,0,-1):
        print("*",end="")
    for j in range(2*(5-i)):
        print(" ",end="")
    for j in range(i,0,-1):
        print("*",end="")
    print()
    
for i in range(5):
    for j in range(i+1):
        print("*",end="")
    for j in range(2*(4-i)):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()
