string,f=map(str,input().split())
if f in string:
    print(string.count(f))


# Each charachter frequency
string1=input()
for i in string1:
    f=string1.count(i)
    print(f'{i} is {f} time(s) in the string')