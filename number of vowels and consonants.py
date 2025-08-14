n=input()
vowels={'a','e','i','o','u','A','E','I','O','U'}
vcount=0
ccount=0
for i in n:
    if i.isalpha():
        if i in vowels:
            vcount+=1
        else:
            ccount+=1
print("vowels count",vcount)
print("consonent count",ccount)

#Input:
'Hello World'
# Output:
'''vowels count 3
consonent count 7'''
        
