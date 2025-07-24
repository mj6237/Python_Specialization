'''
Malicious Keyword Detector (Single Word) 
o Create a simple program that asks the user to input a sentence or a log entry. 
o Define a variable holding a "malicious" keyword (e.g., malicious_keyword = "attack"). 
o Use a condition and string method to check if the input sentence contains the malicious keyword (case
insensitive). 
o Print "Potential threat detected!" or "No threat detected."

'''
malicious_keyword = "attack"
user_input = input("Enter your command :").lower()
    
if malicious_keyword in user_input :
    print("Potential threat detected")
else :
    print("No threat detected")
        