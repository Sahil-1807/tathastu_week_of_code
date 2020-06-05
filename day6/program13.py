n=[x for x in input("enter the numbers seperated by comma").split(",")]
N=[]
for a in n:
    n.remove(a)
    for b in n:
        n.remove(b)
        for c in n:
            if 1<float(float(a)+float(b)+float(c))<2:
                if float(a)+float(b)+float(c) not in N:
                    print("numbers are a=",a," b=",b,"c=",c," and their sum is",float(a)+float(b)+float(c))
                    N.append(float(a)+float(b)+float(c))
        N.append(b)
    N.append(a)
    
        
 
