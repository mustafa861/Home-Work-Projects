# Write a program to solve this age-related riddle!

# Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

# Anton is 21 years old.

# Beth is 6 years older than Anton.

# Chen is 20 years older than Beth.

# Drew is as old as Chen's age plus Anton's age.

# Ethan is the same age as Chen.

# Your code should store each person's age to a variable and print their names and ages at the end.
#  The autograder is sensitive to capitalization and punctuation, be careful! Your solution should
#  look like this (the below numbers are made up -- your solution should have the correct values!):


Anton_age:int=21
Beth_age:int=6+Anton_age
Chen_age:int=20+Beth_age
Drew_age:int=Chen_age+Anton_age
Ethan_age:int=Chen_age

print(f"Anton is {Anton_age} years old.")
print(f"Beth is {Beth_age} Years old.")
print(f"Chen is {Chen_age} Years old.")
print(f"Drew is {Drew_age} Years old.")
print(f"Ethan is {Ethan_age} Years old.")


