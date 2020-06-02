dic={}
n=int(input("enter the number of elements in dictionary"))
for i in range(n):
    key=eval(input("enter the key:"))
    value=eval(input("enter the value:"))
    dic.update({key:value})
print(dic)
print("second largest value is ", sorted(list(dic.values()))[-2])
