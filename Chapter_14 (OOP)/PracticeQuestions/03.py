class InventoryItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def sell(self, num_sold):
        if num_sold > self.quantity:
            print("Not enough items to sell!")
        else:
            self.quantity -= num_sold
            print(f"Sold {num_sold} of {self.name}. Remaining quantity: {self.quantity}")

    def add_stock(self, num_added):
        self.quantity += num_added
        print(f"Added {num_added} to stock. New quantity: {self.quantity}")

item1 = InventoryItem("Laptop", 1200, 5)
print(f"Total value of {item1.name}: ${item1.total_value()}")

item1.sell(3)

item1.sell(4)

item1.add_stock(10)

print(f"Final quantity of {item1.name}: {item1.quantity}")
