#  Check if a triangle is valid or not using 3 sides (sum of any 2 > third)

side1 = int(input("Enter first side :"))
side2 = int(input("Enter second side :"))
side3 = int(input("Enter third side :"))

if (side1 + side2) > side3 and (side1 + side3) > side2 and (side2 + side3 > side1):
    print("Triangle is valid")
else:
    print("triangle is not valid")

