
total_price = 0
items = int(input("Number of items: "))
while items < 0:
    print("Invalid number of items")
    items = int(input("How many items do you have?: "))
for i in range(items):
    price = int(input("What is the price of this item?: "))
    total_price += price
if total_price >= 100:
    total_price *= 0.9
print("Your total will be: $", total_price)
