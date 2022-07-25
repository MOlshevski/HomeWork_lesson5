arr = []  # Create an array from 1 to 9
for i in range (1, 10):
    arr.append(i)
print(arr)

value = int(input('Enter the number whose index you want to know - '))

low = 0  # Set the boundaries of the array
high = len(arr) - 1
mid = (low + high) // 2

if value > arr[high]:
    print('You entered the wrong number')

while value != arr[mid]:  # A cycle to determine the index of a number
    if value > arr[mid]:
        low = mid + 1
    elif value < arr[mid]:
        high = mid - 1

    mid = (low + high) // 2

print(f'Index of a number {value} - {mid}')