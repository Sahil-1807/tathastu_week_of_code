N=int(input("enter the number of arrays to be printed"))
list=[]
for i in range(N):
    a=[eval(x) for x in input("enter the elements of list seperated by comma").split(",")]
    a.sort()
    list.append(a)
b=[]
for i in range(N):
    print(list[i])
    b.extend(list[i])
b.sort()
print("list of all sorted list is:",b)
