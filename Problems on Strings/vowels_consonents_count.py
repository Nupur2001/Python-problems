t=int(input())
while t>0:
    S=input().upper()
    vowels_count=0
    consonent_count=0
    vowels=['A','E','I','O','U']

    for char in S:
        if char.isalpha():
            if char in vowels:
                vowels_count+=1
            else:
                consonent_count+=1
    # print("Vowels:",vowels_count)
    # print("Consonents: ",consonent_count)
    print(vowels_count,consonent_count)
    t=t-1