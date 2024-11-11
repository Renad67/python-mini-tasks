i = 0

while i < 7:  # Loop from 0 to 6
    if i == 3 or i == 6:
        i += 1
        continue  # Skip the current iteration if the number is 3 or 6
    print(i, end=" ")  # Print the current number
    i += 1
