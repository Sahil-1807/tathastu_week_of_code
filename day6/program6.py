def circulararray(arr):
    count=0
    length=len(arr)
    for i in range(length):
        if arr[i]>arr[(i+1)%length]:
            count+=1
        return count<=1
arr=[eval(x) for x in input("enter the array element seperated by comma").split(",")]
print("array is sorted and rotated:")
print(circulararray(arr))
            
        
