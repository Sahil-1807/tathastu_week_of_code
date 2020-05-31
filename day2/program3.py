for i in range(1,9):
    for j in range(1,9):
        if j==i or j==9-i:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    
