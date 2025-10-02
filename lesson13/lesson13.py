# Lesson 13
# input
month = int(input("What is the month numerically: "))
if month < 2:
    print("Before Feburary 18th")
elif month > 2:
    print("After February 18th")
else:
    day = int(input("What is the day: "))
    if day == 18:
        print("Special day!")
    elif day < 18:
        print("Before Feburary 18th")
    elif day > 18:
        print("After February 18th")





