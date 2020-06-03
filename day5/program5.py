def sorting(lst,size):
    even=[]
    for i in range(size-1):
        if(lst[i]%2==0):
            even.append(lst[i])
            lst.pop(i)
    lst.sort()
    even.sort()
    even.reverse()
    final=[even,lst]
    return final

     
lst=[eval(x) for x in input("enter the vlues").split(",")]
size=len(lst)
print("final list after sorting is",sorting(lst,size))
