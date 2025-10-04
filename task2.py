# 1. Create a list of integers from 1 to 20
numbers = list(range(1, 21))

# 2. Use a for loop to find numbers divisible by 3
divisible_by_3 = []  # Empty list to store results
for num in numbers:
    if num % 3 == 0:
        divisible_by_3.append(num)

# 3. Print the numbers divisible by 3
print("Numbers divisible by 3:", divisible_by_3)
