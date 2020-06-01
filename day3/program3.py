
n=input("enter the string")
st=""
i=0
for x in n:
    if n.index(x)==i:
        st=st+x
    i=i+1

print("after removing the duplicate letter in string the string is",st)
