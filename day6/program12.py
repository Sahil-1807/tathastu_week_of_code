N=[eval(x) for x in input("enter the strings seperated by comma").split(",")]
size=len(N)
if size==0:
    print("there is no string in array")
if size==1:
    print(arr[0])
N.sort()
end=min(len(N[0]),len(N[size-1])) 
i=0
while i<end:
    if N[0][i]==N[size-1][i]:
        i+=1
        
    else:
        break
print("the common sting in all string is ",N[0][0:i])
