# Problem 2

# 1. Which function returns a number, which returns a string, and which returns a Boolean?
# calculate_average() returns a number (the computed average).
# get_performance() returns a string (the performance remark).
# The eligibility/checking function returns a Boolean (True or False).

# 2. Explain how the average moves from calculate_average() into get_performance().
# calculate_average() returns the computed value and saves it in a variable, which is then passed as an argument when calling get_performance().

# 3. What happens when a student has a high average but has completed fewer than three tasks?
# Even if the average is high, the student still fails the requirement (returns False / not qualified) because they didn't finish at least three tasks.

# 4. Why is return more appropriate than simply printing the result inside each function?
# Using return lets us save and reuse the output in other functions or calculations, whereas print() just displays it on screen and cannot be reused.
