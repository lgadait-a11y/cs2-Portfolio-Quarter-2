Exercise 1

#list of 5 supplies
school_items = ["Notebook", "Pen", "Calculator", "Laptop", "Book"]

# Display all five items without loop
print("All items in my school bag:")
print(school_items[0])  # Index 0 is the first item
print(school_items[1])  # Index 1 is the second item
print(school_items[2])  # Index 2 is the third item
print(school_items[3])  # Index 3 is the fourth item
print(school_items[4])  # Index 4 is the fifth item

# Display the first item separately using Index 0[cite: 1]
print("\nFirst item:", school_items[0])

# Display the last item separately using Index 4[cite: 1]
print("Last item:", school_items[4])

Exercise 2

# list of five travel locations[cite: 1]
destinations = ["Cebu", "Manila", "Davao", "Baguio", "Palawan"]

# Use a for loop to go through the list and print each destination[cite: 1]
print("All destinations:")
for place in destinations:
    print(place)

# Use list slicing [1:4] to display items from index 1 up to (but not including) index 4[cite: 1]
print("\nSliced destinations (index 1 to 3):", destinations[1:4])

# Ask the user to type a destination to search for[cite: 1]
search_place = input("\nEnter a destination to search for: ")

# Check if the user's input exists in the destinations list[cite: 1]
if search_place in destinations:
    print(f"{search_place} is in the list!")
else:
    print(f"{search_place} is not in the list.")

# Replace the item at index 2 ("Davao") with "Iloilo"[cite: 1]
destinations[2] = "Iloilo"

# Display the updated list[cite: 1]
print("\nUpdated destinations list:", destinations)

#For exercise 2 I used ai to help me because I still get confused but I somehwat get it

