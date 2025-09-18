# Lesson 4
# input
count = 0
fence_length = ""
print("Enter fence length in the form of 'F's (3x): ")
while (count < 3):
    fence_length += input()
    count += 1

# process
fence_length = int(len(fence_length))
can_amount_left = fence_length % 12
cost = (fence_length // 12) * 14.95 + (can_amount_left ** 1) * 14.95

# output
print(f"Cans Required: {fence_length}, Cans Leftover: {can_amount_left}, Cost: ${cost}")
