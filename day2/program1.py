
n=int(input("enter the number"))
#odd or even
if n%2==0:
    print("even number")
else:
    print("odd number")
    
#prime number
if n<2:
      print("not a prime number")
else:
      for i in range(2,n):
          if n%i==0:
              print("not prime number")
              break
              
      else:
           print("prime number")

#palindrome 
temp=n
rev=0
while n>0:
     dig=n%10
     rev=rev*10+dig
     n=n//10
if(temp==rev):
     print("number is palindrome")
else:
     print("number is not a palindrome")
        
#armstrong number
temp=n
result=0
N=len(str(n))
while(n!=0):
     dig=n%10
     result=result+dig**N
     n=n//10
if temp==result:
     print("armstrong number")
else:
     print("number is not armstrong number")
