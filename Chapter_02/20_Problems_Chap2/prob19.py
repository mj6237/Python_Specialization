# Ask the user for their birth year and calculate their current age. 

user_dob = int(input("Enter your DOB :"))
current_year = int(input("Enter current year :"))

user_age = current_year - user_dob

print(f"Your current age is {user_age} years")