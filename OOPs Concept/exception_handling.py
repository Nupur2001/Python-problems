a=int(input())
b=int(input())
# b=(input())

try:
    print(a//b)
    # print(a//c)
except Exception as e:
    print(e)

finally:
    print("finally")