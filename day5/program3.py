def thief(house,start):
    stole=0
    for i in range(start,len(house),2):
        stole+=house[i]
    return stole
house=[eval(x) for i in input("enter the house values seperated by comma").split(",")]
if thief(house,0)>thief(house,1):
    print("enter the max vlaue stolen by the theif",thief(house,0))
else:
    print("enter the max value stolen by the thief",thief(house,1))
