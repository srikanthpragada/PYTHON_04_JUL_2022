# Calculate net amount by taking qty and price

price = float(input("Enter price :"))  # convert str to float
qty = int(input("Enter qty :"))  # convert str to int

amount = price * qty
discount = amount * 20 / 100       # 20% discount
after_discount = amount - discount
tax = after_discount * 0.08
net_amount = after_discount + tax

print(f"Amount         {amount:8.2f}")
print(f" -Discount     {discount:8.2f}")
print(f"               {'-' * 8}")        # line
print(f"               {after_discount:8.2f}")
print(f" +Tax          {tax:8.2f}")
print(f"               {'-' * 8}")        # line
print(f"Net Amount     {net_amount:8.2f}")

