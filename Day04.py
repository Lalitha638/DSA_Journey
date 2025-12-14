# simple binary program# Binary Search Program
# Binary Search Program
# Works only on sorted lists

arr = [2, 4, 6, 8, 10, 12, 14]
target = 10

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        print("Element found at index:", mid)
        break
    elif target < arr[mid]:
        high = mid - 1
    else:
        low = mid + 1
else:
    print("Element not found")
 #binary search function version
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1


arr = [1, 3, 5, 7, 9]
print(binary_search(arr, 7))
 #binary search sing user output
arr = list(map(int, input("Enter sorted numbers: ").split()))
target = int(input("Enter element to search: "))

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        print("Found at index:", mid)
        break
    elif target < arr[mid]:
        high = mid - 1
    else:
        low = mid + 1
else:
    print("Not found")
#binary search using recursion
def binary_search(arr, low, high, target):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, low, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, high, target)


arr = [2, 4, 6, 8, 10]
print(binary_search(arr, 0, len(arr) - 1, 8))
 #check elements exits
arr = [10, 20, 30, 40, 50]
target = 25

low = 0
high = len(arr) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        found = True
        break
    elif target < arr[mid]:
        high = mid - 1
    else:
        low = mid + 1

print(found)

#count comparission
arr = [1, 2, 3, 4, 5, 6, 7, 8]
target = 6

low = 0
high = len(arr) - 1
count = 0

while low <= high:
    count += 1
    mid = (low + high) // 2

    if arr[mid] == target:
        print("Found in", count, "steps")
        break
    elif target < arr[mid]:
        high = mid - 1
    else:
        low = mid + 1

