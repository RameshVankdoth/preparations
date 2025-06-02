import time

from memory_profiler import profile

arr = [10, 5, 20, 30, 25, 13, 18, 15]


@profile
def bubble(arr):
    t1 = time.time()
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    t2 = time.time()
    print("Total time taken:", t2 - t1)
    return arr


print(bubble(arr))
