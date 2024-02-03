def rgb_to_hex(red,green,blue):
    return "#{:02x}{:02x}{:02x}".format(red,green,blue).upper()
red_values,green_values,blue_values=map(int,input("Enter the value of red green and blue: ").split())

hc=rgb_to_hex(red_values,green_values,blue_values)
print(f'Hex code for red={red_values}, green={green_values}, and blue={blue_values} is {hc}')


def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    return tuple(int(hex_code[i:i + 2], 16) for i in (0, 2, 4))

hex_input = input("Enter a hexadecimal color code: ")
rgb_values = hex_to_rgb(hex_input)

print(f'RGB values for {hex_input} are {rgb_values}')
