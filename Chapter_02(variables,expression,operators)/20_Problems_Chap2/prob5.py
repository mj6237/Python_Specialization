# Take input for a temperature in Celsius and convert it to Fahrenheit.

temp_in_cel = float(input("Enter temperature in Celsius : \n"))
temp_in_fehr = (temp_in_cel * 9/5) + 32
print(f"{temp_in_cel}C is equal to {temp_in_fehr}F")