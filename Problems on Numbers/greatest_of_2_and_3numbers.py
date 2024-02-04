n,m=map(int,input().split())
if n>m:
    print(f'{n} is greater than {m}')
else:
    print(f'{m} is greater than {n}')

    
a,b,c=map(int,input().split())
if a>b and a>c:
    print(f'{a} is greater than {b} and {c}')
elif b>a and b>c:
    print(f'{b} is greater than {a} and {c}')
elif c>a and c>b:
    print(f'{c} is greater than {a} and {b}')
else:
    print("Invalid")
    
    