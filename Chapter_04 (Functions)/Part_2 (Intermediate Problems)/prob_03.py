'''
Define a function tax(income) 
Return: 
 0 if income ≤ 25,000 
 5% of income if 25K-50K 
 10% if 50K-100K 
 15% if above 100K 
Return the tax amount (not the total income). 

'''
def tax(income) :
    if income <= 25000 :
        return 0
    elif income > 25000 and  income < 50000 :
        return (income / 100 * 5)
    elif income > 50000 and income < 100000 :
        return (income / 100 * 10)
    else :
        return (income / 100 * 15)

income = int(input("Enter your income :"))
total_tax = tax(income)
print(f"Your Tax is : {total_tax}")
