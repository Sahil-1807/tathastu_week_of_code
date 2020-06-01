mylist=[eval(x) for x in input("enter your elements seperated by comma").split(",")]
print(mylist)
print("remove the duplicate character from mylist")
x=set(mylist)
mylist1=list(x)
print("after removing the double character from mylist the list is",mylist1)  
