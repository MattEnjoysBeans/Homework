# Lesson 11
# input
coordinate = input("Enter the coordinates (x y): ")
coordinate = coordinate.split(' ')

coordinate = list(map(int, coordinate))

x, y = coordinate

if x < 0:
    if y < 0:
        print(f"{coordinate} is in Quadrant 3")
    else:
        print(f"{coordinate} is in Quadrant 2")
else:
    if y < 0:
        print(f"{coordinate} is in Quadrant 4")
    else:
        print(f"{coordinate} is in Quadrant 1")