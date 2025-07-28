'''
What the Question Demands: 
1. Ask the user for the temperature (integer). 
2. If temperature is above 30, print "It's very hot! Stay indoors." 
3. Else if temperature is between 20 and 30 (inclusive), print "It's pleasant. Enjoy outside!" 
4. Else if temperature is between 10 and 19 (inclusive), print "It's cool. A light jacket might be good." 
5. Otherwise (below 10), print "It's cold! Dress warmly."
'''

temp = int(input("Enter current temperature :"))

if temp >= 30 :
    print("It's hot, Stay indoors.")
elif temp >= 20 and temp <= 30 :
    print("It's pleasant. Enjoy outide !") 
elif temp >= 10 and temp < 20 :
    print("It's cool. A light Jacket might be good.")
else :
    print("It's cold! Dress warmly.")