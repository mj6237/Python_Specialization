''' Write a program which prompts the user for a Celsius temperature, convert the 
temperature to Fahrenheit, and print out the converted temperature.'''

temp_in_cel = float(input("Enter temperature in Celsius : \n"))
temp_in_fahr = ((temp_in_cel * 9/5) +32 ) # This is formula for converting Celsius to Fehrenheit
print (f"{temp_in_cel} C is equal to {temp_in_fahr} F")