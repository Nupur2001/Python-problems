'''
You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
number of cans = (wall height x wall width) + coverage per can.
e.g. Height = 2, Width = 4, Coverage = 5
number of cans = (2 \* 4) / 5
= 1.6
But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.
IMPORTANT: Notice the name of the function and parameters must match those on line 13 for the code to work.
Example Input
3
9
Example Output
You '11 need 6 cans of paint.
'''

def paint_wall():
    height=float(input("Enter height of the wall: "))
    width=float(input("Enter width of the wall: "))
    coverage=float(input("Enter coverage of the wall: "))
    number_of_cans=round((height*width)/coverage,2)
    print(f'{number_of_cans} cans are required to paint the wall')

paint_wall()

def wall_paint(h,w,c):
    number_of_cans=round((h*w)/c,2)

    print(number_of_cans)
wall_paint(2,4,5)


