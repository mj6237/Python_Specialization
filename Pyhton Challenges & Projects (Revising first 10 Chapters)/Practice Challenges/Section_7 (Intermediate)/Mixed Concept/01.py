'''
1. Initialize a dictionary user_profile = {"name": "Guest", "email": "guest@example.com", 
"status": "offline"}. 
2. Define a function display_profile(profile) that prints all key-value pairs of the profile dictionary 
neatly. 
3. Define a function update_profile(profile, key, new_value) that updates a specific key in the 
profile dictionary with new_value. Print a confirmation message. 
4. Call display_profile to show the initial profile. 
5. Call update_profile to change the name to "Alice" and status to "online". 
6. Call display_profile again to show the updated profile.
'''
def display_profile(profile):
    print(f"Name: {profile['name']}")
    print(f"Email: {profile['email']}")
    print(f"Status: {profile['status']}")

def update_profile(profile, key, new_value):
    profile[key] = new_value
    print(f"{key.capitalize()} updated to: {new_value}")

# Initialize profile
user_profile = {
    "name": "Guest",
    "email": "guest@example.com",
    "status": "offline"
}

# Display initial profile
display_profile(user_profile)

# Update name and status
update_profile(user_profile, "name", "Alice")
update_profile(user_profile, "status", "online")

# Display updated profile
display_profile(user_profile)


