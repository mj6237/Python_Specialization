'''
1. Define a function named greet_default that takes one parameter name, with a default value of "Guest". 
2. Inside the function, print "Welcome, [name]!". 
3. Call greet_default once without any argument. 
4. Call greet_default once with a specific name (e.g., "Sarah").
'''

def greet_default(name="Guest") :
    print(f"Hi {name}")

greet_default()
greet_default("Sarah")