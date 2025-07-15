'''
Define a function to_celsius(f) that: 
 Takes Fahrenheit as input 
 Converts to Celsius using formula: 
C = (F − 32) × 5/9 
 Returns the result (rounded to 2 decimal places) 
'''

def to_celsius(f) :
    celsius = (f - 32) * 5/9
    return celsius
f = float(input(f"Enter temperature in Fehrenheit :"))
temp_in_celsius = to_celsius(f)
print(f"Temperature in Celsius is : {temp_in_celsius:.2f} C")