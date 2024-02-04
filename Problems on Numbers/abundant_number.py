def abundant_no():
    t=int(input("Enter the number of test case: \n"))
    while t>0:
        n=int(input())
        divisors=[]
        sum=0
        for i in range(1,n):
            if n%i==0:
                divisors.append(i)
                sum+=i

        print(f"Divisors: {divisors}")
        print(f"Sum of divisors: {sum}")
        if sum > n:
            print(f"{n} is an abundant number")
        else:
            print(f"{n} is not an abundant number") 
        t=t-1

if __name__ == "__main__":
    abundant_no()

