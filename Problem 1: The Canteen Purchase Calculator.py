def calculate_total(price, quantity):
  return price * quantity 

def calculate_change(payment, total_cost):
  return payment - total_cost

price = float(input("Enter Item Price: "))
quantity = int(input("Enter Quantity: "))
payment = float(input("Enter Amount Paid: "))

total_cost = calculate_total(price, quantity)
change = calculate_change(payment, total_cost)

print(f"Total Cost: PHP {total_cost:.2f}")

if change >= 0:
  print(f"Change: PHP {change:.2f}")
