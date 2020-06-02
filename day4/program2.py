list_tuple=[(1,2,3),(4,5,2),(2,3,1),(9,6,2),(2,3,8)]
print("show the list touple before sorting",list_tuple)
N=int(input("enter the nth value of tuple from which you want to sort list tuple"))
x=sorted(list_tuple, key=lambda p:p[N-1])
print("sorted list touple is ",x)
    
