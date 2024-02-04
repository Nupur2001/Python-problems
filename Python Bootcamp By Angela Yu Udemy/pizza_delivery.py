'''
Instructions
Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.
Based on a user's order, work out their final bill.
Small pizza (S): $15
Medium pizza (M): $20
Large pizza (L): S25
Add pepperoni for small pizza (Y or N): +$2
Add extra cheese for any size pizza (Y or N): +$1
Example Input
L
Y
N
Example Output
Thank you for choosing Python Pizza Deliveries!
Your final bill is: $28.
'''

print("Welcome to Pizza Cafe")
size=str(input("Enter the size of the pizza you want,Sir:\n Small pizza (S) = $15\n Medium pizza (M) = $20\n Large pizza (L) = $25\n").upper())
add_pepperoni=str(input("Add pepperoni for small pizza (Y or N): +$2").upper())
add_cheese=str(input("Add extra cheese for any size pizza (Y or N): +$1").upper())

if size=="S":
    cost=15
elif size=="M":
    cost=20
elif size=="L":
    cost=25
else:
    print("Enter valid size")
    exit()

if add_pepperoni=="Y":
    cost+=2
else:
    pass

if add_cheese=="Y":
    cost+=1
else:
    pass

print(f"Thank you for choosing Pizza Cafe!\nYour final bill is: ${cost}")








