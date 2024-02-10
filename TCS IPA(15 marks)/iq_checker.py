# calculate iq using age and health number
# iq = (healthnumber/ age) *100

#     INPUT
# 3
# 1 ->serial no
# anmol ->name
# 181 ->mental health
# 24 ->age
# 2
# james
# 236
# 34
# 3
# peter
# 160
# 20
#     OUTPUT
# 1 anmol 754.16
# 2 james 694.11
# 3 peter 800.00


name=(input())
mental_health=int(input())
age=int(input())
iq=(mental_health/age)*100
iq_rounded=round(iq,2)
print(f'The iq of {name} at the age of {age} is {iq_rounded}')


n=int(input())
for i in range(n):
    s_no=int(input())
    name=(input())
    mental_health=int(input())
    age=int(input())
    iq=(mental_health/age)*100
    iq_rounded=round(iq,2)
    print(f'The iq of {name} at the age of {age} is {iq_rounded}')

