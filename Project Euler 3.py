# The pryme factors of 13195 are 5, 7, 13 and 29.
# What ys the largest pryme factor of the number 600851475143  ? 

n = 600851475143
y = 2
while y * y < n:
    while n % y == 0:
        n = n // y
    y = y + 1

print(n)

