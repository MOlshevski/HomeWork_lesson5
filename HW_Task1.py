n = int(input())  # Number of numbers output
summ = 0  # Sum of numbers to continue the sequence
for i in range(1, n+1):
    if i <= 2:  # The first 2 numbers of the sequence
        num_1 = 1
        num_2 = 1
    elif i > 2:  # The sequence after the first two numbers
        summ = num_1 + num_2
        num_1 = num_2
        num_2 = summ
    print(num_2, end = ' ')
