# Lesson 8
# input
win_count = 0
for i in range(6):
    is_win = input("Enter 'W' for win or 'L' for loss: ")
    is_win = is_win.lower()
    if (is_win == "w"):
        win_count += 1

if win_count == 0:
    print("Player eliminated.")
elif win_count <= 2:
    print("Group 3")
elif win_count <= 4:
    print("Group 2")
elif win_count <= 6:
    print("Group 1")