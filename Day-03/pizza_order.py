# Pizza Order
# Instructions
# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
#
# Based on a user's order, work out their final bill.
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1
#
# Example Input
# size = "L"
# add_pepperoni = "Y"
# extra_cheese = "N"
# Example Output
# Your final bill is: $28.

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
if size == 'S':
    bill += 15
    print("Adding $15 for small pizza")
    if add_pepperoni == 'Y':
        bill += 2
        print("Adding $2 for pepperoni")
elif size == 'M':
    bill += 20
    print("Adding $20 for medium pizza")
    if add_pepperoni == 'Y':
        bill += 3
        print("Adding $3 for pepperoni")
else:
    bill += 25
    print("Adding $25 for large pizza")
    if add_pepperoni == 'Y':
        bill += 3
        print("Adding $3 for pepperoni")

if extra_cheese == 'Y':
    bill += 1
    print("Adding $1 for extra cheese")

print(f"Your final bill is: ${bill}.")
