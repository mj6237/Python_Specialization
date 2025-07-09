# Ask the user for the price and quantity of an item and calculate the total cost.

price = int(input("Enter price of the item per kg : "))
quantity = float(input("How much kgs you want to buy :"))
total = price * quantity
print(f"Your total bill is : Rs.{total:.2f}")