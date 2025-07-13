# Define a function area_of_circle(radius) that returns area (πr²) 

import math

def area_of_circle(radius) :
    return math.pi * radius **2
radius = int(input("Enter radius of the circle :"))
area = area_of_circle(radius)
print(f"Area of the circle is : {area:.2f}")