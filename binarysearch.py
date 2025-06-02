arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def binary(arr, target):
    start = 0
    end = len(arr)
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
    return -1


print(binary(arr, 8)) 
