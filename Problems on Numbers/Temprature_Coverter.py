# Temprature Conversion

# Celsius to Fahrenheit

def Celsius_to_Fahrenheit():
    c=int(input("Enter temperature in degrees Celsius: "))
    print(f'Temperature in degrees Fahrenheit: {(9/5)*c+32}F')

print(Celsius_to_Fahrenheit())

# Celsius to Kelvin
def Celsius_to_Kelvin():
    c=int(input("Enter temperature in degrees Celsius: "))
    print(f'Temperature in degrees Kelvin: {c + 273.15}K')
print(Celsius_to_Kelvin())

# Fahrenheit to Celsius 
def Fahrenheit_to_Celsius ():
    f=int(input("Enter temperature in degrees Fahrenheit: "))
    fr=format((f-32) * 5/9,'.2f')
    # format(number, ".2f")
    print(f'Temperature in degrees Celsius: {fr}C')
print(Fahrenheit_to_Celsius())

# Fahrenheit to Kelvin
def Fahrenheit_to_Kelvin ():
    f=int(input("Enter temperature in degrees Fahrenheit: "))
    fk=format((f - 32) * 5/9 + 273.15,'.2f')
    print(f'Temperature in degrees Kelvin: {fk}K')
print(Fahrenheit_to_Kelvin())



