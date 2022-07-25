def fact(n):
    if n == 1:
        return n
    else:
        return n*fact(n-1)

n = int(input('Enter the number - '))

print(f'The factorial of a number {n} is equal to {fact(n)}')
