n=input()
vowels=['a','A','e' , 'E' , 'i' , 'I' , 'o' , 'O' , 'u' , 'U']
result=""
for i in range(len(n)):
    if n[i] not in vowels:
        result=result+n[i]
print(result)