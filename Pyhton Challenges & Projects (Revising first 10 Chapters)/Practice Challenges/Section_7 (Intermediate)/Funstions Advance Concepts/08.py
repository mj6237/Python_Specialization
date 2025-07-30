'''
1. Define a function get_user_setting(user_settings, setting_name, default_value) that takes a 
dictionary user_settings, a setting_name (key), and a default_value. 
2. Return the value of setting_name from user_settings. If setting_name is not found, return 
default_value. 
3. Create a sample user_config = {"theme": "dark", "font_size": 12}. 
4. Call the function to get "theme" (should return "dark"). 
5. Call the function to get "language" with a default of "English" (should return "English"). 
6. Print both results.
'''

def get_user_setting(user_settings, setting_name, default_value):
    return user_settings.get(setting_name, default_value)

# Sample dictionary
user_config = {"theme": "dark", "font_size": 12}

# Call the function
theme = get_user_setting(user_config, "theme", "light")         # should return "dark"
language = get_user_setting(user_config, "language", "English") # should return "English"

# Print results
print("Theme:", theme)
print("Language:", language)
