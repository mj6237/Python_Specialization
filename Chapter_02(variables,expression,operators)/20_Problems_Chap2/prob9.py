# Ask the user for the radius of a circle and calculate its area (area = π * r^2). 

import math

r = float(input("Enter radius of the circle :"))
area = math.pi * r**2
print(f"Area of the Circle is :{area}")

#To limit the result to 2 decimal places
print(f"Area of the Circle is :{area:.2f}")