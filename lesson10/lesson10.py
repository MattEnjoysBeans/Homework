# Lesson 10
# input
phone = input("Enter the last four digits of the number: ")

if phone[0] in {"8","9"}:
    if phone[3] in {"8","9"}:
        if phone[1] == phone [2]:
            print(f"{phone} is a Telemarketer")
        else: print(f"{phone} is not a Telemarketer")
    else: print(f"{phone} is not a Telemarketer")
else: print(f"{phone} is not a Telemarketer")