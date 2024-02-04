def Palindrome(n):
    n_str=str(n)
    return n_str==n_str[::-1]


start,end=map(int,input().split())
palindrome=[]

for n in range(start,end+1):
    if Palindrome(n):
        palindrome.append(n)
        


if len(palindrome)>0:
    print(f"Palindrome numbers between {start} to {end} is/are: ")
    p=' '.join(map(str,palindrome))
    print(p)
else:
    print("No palindrome numbers found")
