ch=input()
brackets=['(',')','{','}','[',']']
for bracket in brackets:
    ch=ch.replace(bracket,"")
print(ch)