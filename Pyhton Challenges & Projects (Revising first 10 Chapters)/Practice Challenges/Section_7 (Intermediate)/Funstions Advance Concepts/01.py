'''
1. Define a function send_notification(message, recipient="Admin", type="info") that takes a 
message (required) and two optional parameters: recipient (default "Admin") and type (default "info"). 
2. Inside the function, print a formatted message like "[TYPE] To: RECIPIENT - MESSAGE". 
3. Call the function three times: 
 Only with a message. 
 With a message and a recipient. 
 With a message, recipient, and type.
'''
def send_notification(message, recipient="Admin", type="info") :
    print(f"{type} To: {recipient} - {message}")


send_notification(message="Are you ready ?")
send_notification(message="Are you ready ?", recipient="Joe")
send_notification(message="Are you ready ?", recipient="Joe", type="Question")