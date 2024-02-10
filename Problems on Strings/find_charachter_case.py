## Read input as specified in the question.
## Print output as specified in the question.
t=int(input())
while(t>0):
    ch=input()
    if ch=='A'or ch=='B' or ch=='C'or ch=='D' or ch=='E'or ch=='F' or ch=='G'or ch=='H' or ch=='I'or ch=='J' or ch=='K'or ch=='L' or ch=='M' or ch=='N' or ch=='O'or ch=='P' or ch=='Q'or ch=='R' or ch=='S'or ch=='T' or ch=='U'or ch=='V' or ch=='W'or ch=='X' or ch=='Y'or ch=='Z':
        print("1")
    elif ch=='a'or ch=='b' or ch=='c'or ch=='d' or ch=='e'or ch=='f' or ch=='g'or ch=='h' or ch=='i'or ch=='j' or ch=='k'or ch=='l' or ch=='m'or ch=='n' or ch=='o'or ch=='p' or ch=='q'or ch=='r' or ch=='s'or ch=='t' or ch=='u'or ch=='v' or ch=='w'or ch=='x' or ch=='y'or ch=='z':
        print("0")
    else:
        print("-1")
    t=t-1