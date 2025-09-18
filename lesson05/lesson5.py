# Lesson 5
# input
user_value = float(input("How much money do you have?: "))
user_value -= user_value % 0.01

cookie_amount = input("Enter amount of cookies (in the form of 'bcbcbc'): ")
cookie_amount = cookie_amount.lower()

# processing
big_count = cookie_amount.count("b")
normal_count = cookie_amount.count("c")

cookies_sold = big_count + normal_count
profit = (1.25 * normal_count + 2 * big_count) - (0.5 * normal_count + 0.75 * big_count)
user_value += profit

# output
print(f"Total cookies sold: {cookies_sold}\nTotal Profit: {profit}\nNew Balance: {user_value}")