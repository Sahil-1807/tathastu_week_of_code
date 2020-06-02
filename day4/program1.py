a=eval(input("enter the values seperated by comma"))
print(a)
element=eval(input("enter the element to be search"))
count=0
for i in a:
    if i==element:
         count=count+1
         
print("{} has occurred {} times".format(element,count))
