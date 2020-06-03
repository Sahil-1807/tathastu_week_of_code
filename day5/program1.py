def replace0(number):
    number+=addvalue(number)
    return number

def addvalue(number):
    result=0
    decimalplace=1
    
    if number==0:
        result+=(5*decimalplace)
    
    while number>0:
        if number%10==0:
            result+=(5*decimalplace)
        
        number//=10
        decimalplace*=10
    return result

n=int(input("enter the value you want to change"))
print("the changed value is:",replace0(n))
