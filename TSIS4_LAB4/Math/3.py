# Write a Python program to calculate the area of regular polygon.
import math

def polygon_area(n, side_length):
    return (n * side_length**2) / (4 * math.tan(math.pi / n))

n = int(input("Input number of sides: "))
side_length = float(input("Input the length of a side: "))

area = polygon_area(n, side_length)
print(f"The area of the polygon is: {area:.2f}")
