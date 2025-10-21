import math

def calculate_area_in_acres(radius_in_feet):
    area_in_square_feet = math.pi * radius_in_feet ** 2
    area_in_acres = area_in_square_feet / 43560
    return area_in_acres

radius_in_feet = float(input("Enter the radius of the field in feet: "))
area_in_acres = calculate_area_in_acres(radius_in_feet)
print(f"The area of the field is: {area_in_acres:.2f} acres")
