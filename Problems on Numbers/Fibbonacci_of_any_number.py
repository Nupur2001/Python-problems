def Fibbonacci(n):
    # n=int(input())
    if n<=0:
        print("Enter positive number")
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return Fibbonacci(n-1)+Fibbonacci(n-2)
print(Fibbonacci(int(input())))



    