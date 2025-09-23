# Lesson 7
import random
# input
diff_class = int(input("Enter the Difficulty Number: "))
ability_num = random.randrange(1, 20)

if ability_num >= diff_class:
    print(f"Success (Rolled a {ability_num})")
else:
    print(f"Not powerful enough... (Rolled a {ability_num})")
