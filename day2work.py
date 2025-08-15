'''n=int(input())
count=0
for i in range(1,n+1):
    if(n%i==0):
        count+=1
        
if(count==2):
    print("Prime number")
else:
    print("Not Prime number")'''
#Input:3
#Output:Prime number

'''n=int(input())
fact=1
for i in range(1,n+1):
    fact=fact*i
print("factorial:",fact)'''
#Input:6
#Output:factorial: 720

'''n=int(input())
a=0
b=1
print(a,b,end='')
for i in range(2,n):
    c=a+b
    print(c,end='')
    a=b
    b=c'''
#Input:2
#Output:0 1

'''n=int(input())
sum=0
while n>0:
    rem=n%10
    sum=sum+rem
    n=n//10
print("sum of digits:",sum)'''
#Input:10
#Output:sum of digit: 1

n=int(input())
rev=0
while n>0:
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
print(rev)
#Input:123
#Output:321
    
