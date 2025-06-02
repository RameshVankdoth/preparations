def two_sum(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        diff = target - num
        if diff in seen:
            return (seen[diff], i)
        seen[num] = i
    return []


print(two_sum([1, 2, 3, 4, 5, 6, 7], 10))
