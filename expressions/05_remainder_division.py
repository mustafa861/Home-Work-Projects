# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

# Here's a sample run of the program (user input is in bold italics):

# Please enter an integer to be divided: 5

# Please enter an integer to divide by: 3

# The result of this division is 1 with a remainder of 2


dividend = int(input("Enter the dividend (number to be divided): "))
divisor = int(input("Enter the divisor (number to divide by): "))

# Perform calculations
quotient = dividend // divisor  # Integer division
remainder = dividend % divisor  # Modulo (remainder)

# Display results
print("\n=== Division Result ===")
print(f"{dividend} ÷ {divisor} = {quotient} ")
print(f"The Quotient for {dividend} divided by {divisor} is {quotient} and Remainder is {remainder}")


