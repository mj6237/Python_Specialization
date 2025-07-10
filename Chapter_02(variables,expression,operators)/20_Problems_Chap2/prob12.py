# Write a BMI calculator using: BMI = weight / (height ** 2) 

weight = float(input("Enter your weight in kgs :"))
height = float(input("Enter your height in inches :"))
height_in_meters = height * 0.0254 # 1 meter = 0.0254 inches
print(f"Your height in meters :{height_in_meters}")
bmi = weight / (height_in_meters ** 2)
print(f"Your BMI is : {bmi:.2f}")