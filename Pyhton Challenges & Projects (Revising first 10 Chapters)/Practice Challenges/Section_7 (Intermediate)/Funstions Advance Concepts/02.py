'''
1. Define a function create_user_profile(name, age, email) that takes three parameters. 
2. Inside the function, print the user's details. 
3. Call create_user_profile twice: 
 Once using positional arguments (e.g., ("John", 30, "john@example.com")). 
 Once using keyword arguments, with the arguments in a different order (e.g., email="jane@example.com", 
name="Jane", age=25). 
'''
def create_user_profile(name, age, email) :
    print(f"Name: {name} Age: {age} Email: {email}")


create_user_profile("Joe", 24, "joe123@gmail.com")

create_user_profile(name="Jonny", age=30, email="jonny123@gmail.com")