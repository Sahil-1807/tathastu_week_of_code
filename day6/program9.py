N=[eval(x) for x in input("enter the values seperated by comma").split(",")]
k=eval(input("enter the value of k"))
N.sort()
print("the kth smallest value is:",N[k-1])
