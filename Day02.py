#linear search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
print(linear_search([10, 20, 30, 40], 30))

#using while loop
def linear_search(arr, target):
    i = 0
    while i < len(arr):
        if arr[i] == target:
            return i
        i += 1
    return -1
print(linear_search([3, 9, 4, 2], 3))

# searching smallest Element
def find_smallest(arr):
    smallest = arr[0]
    for x in arr:
        if x < smallest:
            smallest = x
    return smallest
print(linear_search([9,4,5,6,7],[9] ))

#searching largest elements
def find_largest(arr):
    largest = arr[0]
    for x in arr:
        if x > largest:
            largest = x
    return largest

#reverse elements
def reverse_search(arr, target):
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == target:
            return i
    return -1
print(linear_search([1,2,3,4,5], 3))



