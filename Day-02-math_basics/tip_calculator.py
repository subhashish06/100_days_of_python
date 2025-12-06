"""
If the bill was $150.00, split between 5 people, with 12% tip.
Each person should pay (150.00 / 5) * 1.12 = 33.6
Format the result to 2 decimal places = 33.60
Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
HINT:
https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
"""

print("Welcome to the tip calculator.")

# Get the total bill amount from the user and convert it to a float
bill = float(input("What was the total bill? $"))

# Get the desired tip percentage and convert it to an integer
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

# Get the number of people to split the bill and convert it to an integer
ppl = int(input("How many people to split the bill? "))

# Calculate the share per person:
# 1. Convert tip percentage to a decimal (e.g., 12 becomes 0.12)
# 2. Add 1 to represent the total multiplier (e.g., 1.12)
# 3. Divide the bill by the number of people
# 4. Multiply by the tip multiplier
share = bill / ppl * (1 + tip / 100)

# Format the result to 2 decimal places using string formatting
SHARE = "{:0.2f}".format(share)

print("+" * 20 + " Calculating " + "+" * 20)
# Print the final amount each person should pay
print(f"Each person should pay: ${SHARE}")
