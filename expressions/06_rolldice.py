# Simulate rolling two dice, and prints results of each roll as well as the total.

import random

# Define number of sides on a die
DICE_SIDES = 6

# Roll two dice
die1 = random.randint(1, DICE_SIDES)  
die2 = random.randint(1, DICE_SIDES)  
total = die1 + die2  


print("\n=== Dice Roll Simulation ===")
print(f"Die 1: {die1}")
print(f"Die 2: {die2}")
print(f"Total: {total}")


