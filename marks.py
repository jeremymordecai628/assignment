#!/usr/bin/python3

# --- Task 1: Marks average ---

# Get marks from the user
mark_1 = float(input("Enter mark one: "))
mark_2 = float(input("Enter the second mark: "))
mark_3 = float(input("Enter the third mark: "))


# Calculate average
average = (mark_1 + mark_2 + mark_3) / 3

print(f"Average = {average:.2f}")

# Determine result based on average
if average >= 80:
    print("Result: Pass")
elif 50 <= average <= 70:
    print("Result: Average")
elif 0 <= average <= 40:
    print("Result: Good trial")
else:
    print("Invalid marks entered.")

# --- Task 2: Items total ---
# Ask the user to enter prices of 4 items
price_1 = float(input(f"Enter price of item  "))
price_2 = float(input(f"Entre the second price"))
price_3 = float(input(f"Entre the third  price"))



# Calculate total
total = (price_1 + price_2 + price_3)
print(f"Total Purchases = {total:.2f}")

# Check delivery condition
if total >= 1500:
    print("You have received free delivery.")
else:
    print("You will pay 150 for delivery.")

