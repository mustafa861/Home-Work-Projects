# Ask the user for a number and print its square (the product of the number times itself).

# Here's a sample run of the program (user input is in bold italics):

# Type a number to see its square: 4

# 4.0 squared is 16.0



user_input:int=int(input ("Enter a number to square :"))
square:int=(user_input*user_input)
print(f"{user_input} square is {square}") 