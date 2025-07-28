'''
1. Define a function display_user_profile(user_data) that takes one parameter, user_data (which will be a dictionary). 
2. Inside the function, print the user's name and age from the user_data dictionary. 
3. Create a sample user dictionary: my_user = {"name": "John Doe", "age": 30}. 
4. Call display_user_profile with my_user.
'''
def display_user_profile(user_data) :
    print(user_data["name"])
    print(user_data["age"])

user_data = {
    "name" : "Fozi",
    "age" : 24
} 

display_user_profile(user_data)
