# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

naturalnum = 0
multiplesof3 = []
multiplesof5 = []

for k in range(1000):
    if naturalnum % 3 == 0:
        multiplesof3.append(naturalnum)
    elif naturalnum % 5 == 0:
        multiplesof5.append(naturalnum)
    naturalnum += 1

totalnum = sum(multiplesof3) + sum(multiplesof5)
print(totalnum)