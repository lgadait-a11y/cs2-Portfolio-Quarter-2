#   Problemm 1

# 1. What does each function do?
# calculate_total() gets the total bill by multiplying price and quantity.
# calculate_change() gets the sukli (or lacking amount) by subtracting the total from the payment.

# 2. What is the difference between the parameters price and quantity and the actual arguments passed to the function?
# 'price' and 'quantity' are just placeholders inside the function.
# The actual arguments (item_price and item_qty) are the real values typed by the user that get sent into those placeholders.

# 3. Where is the returned total stored, and how is it reused?
# It is stored in 'total_cost'. I reused it to display the total and passed it into calculate_change() to compute the change.

# 4. Why is it useful to separate total calculation from change calculation?
# It keeps the code neat and organized. Each function has one simple job, which makes it easier to debug and reuse later.
