# Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

# Here's a sample run of the program (user input is in bold italics):

# What is the length of side 1? 3

# What is the length of side 2? 4

# What is the length of side 3? 5.5

# The perimeter of the triangle is 12.5
    

length_side1 = float(input("Enter first side length: "))
length_side2 = float(input("Enter second side length: "))
length_side3 = float(input("Enter third side length: "))

    # Calculating perimeter
perimeter = length_side1 + length_side2 + length_side3

    # Displaying the result
print(f"\nThe perimeter of the triangle is {perimeter}\n")


 