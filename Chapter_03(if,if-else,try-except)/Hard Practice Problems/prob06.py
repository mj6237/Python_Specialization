'''
Ask user to enter one character: 
 If character is "+" or "-" → print "Math operator" 
 If "@" or "#" → print "Special symbol" 
 Else → print "Other character"  
'''
chr = input("Enter a character from (+,-,@,#) to check to which family it belongs to :")
try :
    
    if chr == '+' or chr == '-' or chr == '@' or chr == '#' :
        if chr == '+' or chr == '-' :
            print("Math operator")
        else :
            print("Special symbol")
    else :
        print("Enter Character from given list !")        
except ValueError :
    print("Enter Character from given list !")