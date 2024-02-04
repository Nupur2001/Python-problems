def last_digit():
    result=0
    n=int(input())
    while n:
        remainder=n%10
        n=n%10
        result=result*10+remainder
        return result
print(last_digit())