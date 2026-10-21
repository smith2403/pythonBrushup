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