dic={}
n=int(input("enter the number of elements in dictionary"))
for i in range(n):
    key=eval(input("enter the key:"))
    value=[eval(x) for x in input("enter the value:").split(",")]
    dic.update({key:value})
print(dic)
dic1={}
for key,value in dic.items():
    dic1[key]=list(set(value))
print("enter the dictionary without duplicate values",dic1)
