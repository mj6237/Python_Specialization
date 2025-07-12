'''
Triangle Type Identifier (Using Sides) 
Ask for 3 sides: 
 All equal → "Equilateral" 
 Two equal → "Isosceles" 
 All different → "Scalene" 
 Invalid triangle → "Not a triangle" 
'''
side1 = int(input("Enter first side :"))
side2 = int(input("Enter second side :"))
side3 = int(input("Enter third side :"))
if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    if side1 == side2 == side3 :
        print("Equilateral")
    elif (side1 == side2 and side2 != side3) or (side2 == side3 and side2 != side1) or ((side1 == side3 and side3 != side2)):
        print("Isosceles")
    elif side1 != side2 and side1 != side3 and side2 != side3 :
        print("Scalene")
    else :
        print("Not a Triangle !")
else :
    print("Not a valid triangle , Try again !")