t=int(input("Enter the number of test cases: "))
while t>0:
    def leap_year(year):
        if year%4==0 and (year%400==0 or year%100!=0):
            print("Leap year")
        else:
            print("Not a leap year")

    year = int(input("Enter the year: "))
    leap_year(year)
    t=t-1
    

