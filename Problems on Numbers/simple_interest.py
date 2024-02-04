print("Simple Interest Calculator")
def simple_interest(principal,rate,time):
    # principal,rate,time=map(float,input().split())
    amount=(principal*rate*time)/100
    amount_rounded=round(amount,2)
    return amount_rounded
principal,rate,time=map(float,input().split())
result=simple_interest(principal,rate,time)
print("Simple Interest: ",result)

# print(simple_interest(principal=,rate=,time=))