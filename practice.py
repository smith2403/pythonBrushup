# for i in range(1,11):
#     print(i)

# for i in range(10, 0, -2):
#     print(i)

# number divisble by 3
count = 0
for i in range(1, 11):
    if i % 3 == 0:
        count += 1

print(count)

# sum of even numbers
sum = 0
for i in range(1, 11):
    if i % 2 == 0:
        sum += i
print(sum)

# Task: Calculate the sum of all numbers from 1 to 10 that are both:
# - Greater than 5
# - Divisible by 2
sum = 0
for i in range(1, 11):
    if i > 5 and i % 2 == 0:
        sum += i
print(sum)

# Write code to count how many numbers between 1 and 20 (inclusive) are divisible by both 3 and 5.
# Your code should print the count, not the sum.
count = 0
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        count += 1
print(count)


# Task: Count how many numbers between 1 and 30 (inclusive) are divisible by 2 but not divisible by 3.
count = 0
for i in range(1, 31):

    if i % 2 == 0 and i % 3 != 0:
        count += 1
print(count)

# Task: Calculate the sum of all numbers between 1 and 30 that are divisible by 2 but not divisible by 3.
total = 0
for i in range(1, 31):

    if i % 2 == 0 and i % 3 != 0:
        total += i
print(total)

# Write Python code to count how many numbers between 1 and 50 are divisible by 4 or divisible by 7.
c = 0
for i in range(1, 51):

    if i % 4 == 0 or i % 7 == 0:
        c += 1
print(c)

# Write Python code to calculate the sum of numbers from 1 to 50 that are divisible by 4 or 7.
c = 0
for i in range(1, 51):

    if i % 4 == 0 or i % 7 == 0:
        c += i
print(c)

# Task 1: Odd-number loop
# The remainder not being 0 keeps the if condition true. This is because the number is not divisible by 2, so it is an odd number.

# Task 2: Counting even numbers
# Your answer: a — 3
# In each iteration, the loop checks whether the number is divisible by 2. If the condition is true, it adds 1 to the count variable. The numbers 2, 4, and 6 are divisible by 2, so the count becomes 1 + 1 + 1 = 3.

# Task 3: Counting numbers greater than 5
# Your answer: a — 5
# The answer is 5 because 5 > 5 is false. The loop counts the numbers starting from 6 up to 10. Each number satisfies the condition, so the count becomes 1 + 1 + 1 + 1 + 1 = 5.

# Task 4: Summing numbers from 1 to 4
# Your answer: 10
# The loop adds each number to the running total: 0 + 1 = 1, 1 + 2 = 3, 3 + 3 = 6, and 6 + 4 = 10. The final answer is 10.