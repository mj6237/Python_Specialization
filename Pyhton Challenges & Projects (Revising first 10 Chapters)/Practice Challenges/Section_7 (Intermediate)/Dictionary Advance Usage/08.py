'''
1. Create a dictionary: settings = {"theme": "dark", "notifications": True, "sound": "on"}. 
2. Try to delete the key "sound". Print "Sound setting deleted." if successful. 
3. Try to delete the key "language". Use try-except KeyError to catch the error if the key doesn't exist, and 
print "Language setting not found." 
4. Print the settings dictionary after both attempts.
'''
settings = {"theme": "dark", "notifications": True, "sound": "on"}

del settings["sound"]
print("Sound setting deleted.")

try :
    del settings["language"]
except KeyError :
    print("Language setting not found.")

print(settings)