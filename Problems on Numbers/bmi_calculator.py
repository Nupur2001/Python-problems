'''
Underweight: BMI less than 18.5
Normal weight: BMI 18.5 to 24.9
Overweight: BMI 25 to 29.9
Obesity: BMI 30 or greater

Formula
BMI= Weight (kg)/Height (m)**2
 
'''

weight=float(input("Enter your weight in kg: "))
height=float(input("Enter your height in m: "))

BMI=round(weight/(height**2),2)

print(f'Your BMI is {BMI}')

if BMI < 18.5:
    print("You are underweight")
elif 18.5 <= BMI <= 24.9:
    print("You are normal weight")
elif 25 <= BMI < 29.9:
    print("You are overweight")
elif BMI >= 30:
    print("You are obese")
else:
    print("Invalid BMI")

