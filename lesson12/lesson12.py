# Lesson 12
# input
angles = input("Enter the three angles: ")
angles = angles.split(' ')

angles = list(map(int, angles))

a, b, c = angles
total = a + b + c

if a == b == c:
    print("Equilateral Triangle")
elif (a in {b, c} or b in {a, c} or c in {b, a}) and total == 180:
    print("Isoceles Triangle")
elif total == 180:
    print("Scalene Triangle")
else:
    print("Not a triangle")