import math


def area_of_circle():
    r=int(input("Enter the value of radius: "))
    area_circle=math.pi*r*r
    perimeter_circle=math.pi*2*r
    # print(area_circle)
    # print(math.ceil(area_circle))
    print(math.floor(area_circle))
    print(math.floor(perimeter_circle))
    print(f"Area of circle when r={r} is: {math.floor(area_circle)}")
    print(f"Perimeter of circle when r={r} is: {math.floor(perimeter_circle)}")


def area_of_rectangle():
    l,b=map(int,input().split())
    area_rectangle=l*b
    perimeter_rectangle=(l+b)*2
    print(area_rectangle)
    print(f"Area of rectangle when l={l} and b={b} is: {area_rectangle}")
    print(f"Perimeter of rectangle when l={l} and b={b} is: {perimeter_rectangle}")


area_of_circle()
area_of_rectangle()