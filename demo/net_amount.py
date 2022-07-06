# Calculate net amount by taking qty and price

price = float(input("Enter price :"))  # convert str to float
qty = int(input("Enter qty :"))  # convert str to int

amount = price * qty
discount = amount * 20 / 100       # 20% discount
net_amount = amount - discount

print(f"Amount         {amount:8.2f}")
print(f"-Discount      {discount:8.2f}")
print(f"Net Amount     {net_amount:8.2f}")

