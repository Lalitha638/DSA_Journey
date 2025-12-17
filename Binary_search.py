#Binary Search
#1.binary search return the index
def binary_search(arr,target):
    low=0
    high=len(arr)-1

    while low<=high:
        mid=(low+high)//2

        if arr[mid]==target:
         return mid
        elif target<arr[mid]:
         high=mid-1
        else:
         low=mid+1
    return -1
arr=[2,4,6,8,10]
print(binary_search(arr,8))

#2.Binary search Return True /False
def binary_search_bool(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return True
        elif target<arr[mid]:
            high=mid-1
        else:
            low=mid+1
    return False
arr=[3,6,9,12,15,18]
print(binary_search_bool(arr,12))

#3.binary search element not found
def binary_search_bool(arr,target):
    low=0
    high=len(arr)-1
    while low>=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif target<arr[mid]:
            high=mid-1
        else:
            low=mid+1
    return -1
arr=[3,6,9,12,15,18]
print(binary_search_bool(arr,12))

#4.find the first occurence of a target
def binary_search_first_occurrence(arr,target):
    low=0
    high=len(arr)-1
    result=-1
    while  low<=high:
        mid=(low+high)//2
        if arr[mid] == target:
            result = mid
            high = mid-1
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return result
arr=[2,4,4,4,6,8]
print(binary_search_first_occurrence(arr,4))

#5.ind last occurrence of a target
def binary_search_occurrence(arr,target):
    low=0
    high=len(arr)-1
    result=-1
    while low<=high:
        mid=(low+high)//2

        if arr[mid]==target:
            result=mid
            low=mid+1
        elif target<arr[mid]:
            high=mid-1
        else:
            low=mid+1
    return result
arr=[2,2,2,3,4,4,4,4,9]
print(binary_search_occurrence(arr,4))

#Frequently count (how many times target appears)
def first_occurrence(arr, target):
    low = 0
    high = len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            result = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result


def last_occurrence(arr, target):
    low = 0
    high = len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            result = mid
            low = mid + 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result


def frequency_count(arr, target):
    first = first_occurrence(arr, target)
    if first == -1:
        return 0   # target not found
    last = last_occurrence(arr, target)
    return last - first + 1


arr = [2, 4, 4, 4, 4, 6, 8]
print(frequency_count(arr, 4))
















