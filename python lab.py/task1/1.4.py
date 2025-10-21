import math

def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

x_ram = float(input("Enter the X-coordinate of Ram: "))
y_ram = float(input("Enter the Y-coordinate of Ram: "))

x_sita = float(input("Enter the X-coordinate of Sita: "))
y_sita = float(input("Enter the Y-coordinate of Sita: "))

distance_between_them = calculate_distance(x_ram, y_ram, x_sita, y_sita)
print("The distance between Ram and Sita is:", distance_between_them)
