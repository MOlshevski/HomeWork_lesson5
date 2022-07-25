
arr = [5, 6, 7, 1, 2, 3, 4]
print('Source array -', arr)

# Function to find the index of a number in an array
def index(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i

key = int(input('Enter a number from the array - '))

if max(arr) < key:  # Output the index of the number and the record, in case there is no such number in the array
    print('There is no such number in the array')
else:
    print(f'Index of a number {key} - {index(arr, key)}')