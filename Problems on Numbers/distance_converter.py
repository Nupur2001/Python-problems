'''
In this lab, you will create a Python function named convert_distance() to convert distances between kilometers and meters. Your function should take two parameters: distance (a floating-point number) and unit (a string that can either be "km" for kilometers or "mtr" for meters). The function should return a tuple with the converted distance as a floating-point value and the corresponding unit.

Function Requirements:
Input Parameters:
distance: A floating-point number representing the distance.
unit: A string, either "km" or "mtr".
Output:
A tuple: The first element is the converted distance as a float, and the second element is the unit of the converted distance (either "km" or "mtr").
Your function should raise an ValueError when a negative number is passed or when a different unit is passed to the function.

If you're not familiar with ValueError you can read this doc.

If you're faimilar with raising Exceptions, check this pargraph

Examples:
Converting Kilometers to Meters:

Input: distance = 1.5, unit = "km"
Output: (1500.0, "mtr")
This means when you pass 1.5 kilometers to the function, it should return 1500.0 meters.
Converting Meters to Kilometers:

Input: distance = 3000, unit = "mtr"
Output: (3.0, "km")
Here, 3000 meters is converted to 3.0 kilometers.
Remember, your function should also handle edge cases, such as inputting a zero or negative distance, and should behave accordingly as specified in the challenges.


Test cases:
Convert kilometers to meters

Convert meters to kilometers

Handle zero meter input

Raise ValueError for negative values

Raise ValueError for improper unit parameter
'''



def dist_converter(distance, unit):
    """
    Converts a distance between kilometers and meters.

    Parameters:
    - distance (float): The distance to be converted.
    - unit (str): The unit of the distance ('km' or 'mtr').

    Returns:
    - tuple: A tuple containing the converted distance and its unit.
    """

    if distance == 0:
        raise ValueError("Distance cannot be zero.")
    elif distance < 0:
        raise ValueError("Distance cannot be negative.")
    elif unit == 'km':
        distance *= 1000
        return (float(distance), 'mtr')
    elif unit == 'mtr':
        distance /= 1000
        return (float(distance), 'km')
    else:
        raise ValueError("Invalid unit parameter. Please use 'km' or 'mtr'.")

# Example usage:
try:
    input_distance = float(input("Enter distance: "))
    input_unit = str(input("Enter unit (km or mtr): "))
    result = dist_converter(input_distance, input_unit)
    print("Converted Distance:", result)
except ValueError as e:
    print("Error:", e)
