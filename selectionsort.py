arr = [10, 5, 2, 6, 16, 35, 93, 1, 12]
n = len(arr)


def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


print(selection_sort(arr))

# Update
