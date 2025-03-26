# Simulate rolling two dice, three times. Prints the results of each die roll.
#  This program is used to show how variable scope works.


import random

NUM_SIDES = 6


die1 = random.randint(1, NUM_SIDES)  
die2 = random.randint(1, NUM_SIDES)  
total = die1 + die2  
die1, die2, total  


print("🎲 Rolling two dice three times... 🎲\n")

for i in range(1, 4):  
        die1, die2, total 
        print(f"Roll {i}: 🎲 {die1} and 🎲 {die2} (Total: {total})")

print("\n🎲 Done rolling! 🎲")










