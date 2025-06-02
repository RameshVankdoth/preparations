def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    return merge(sortedLeft, sortedRight)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
sortedArr = mergeSort(unsortedArr)
print("Sorted array:", sortedArr)

# Python


def mergesort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    leftarr = arr[:mid]
    rightarr = arr[mid:]

    sortleft = mergesort(leftarr)
    sortright = mergesort(rightarr)

    return merge(sortleft, sortright)


def merge(sortleft, sortright):
    result = []
    i = j = 0
    while i < len(sortleft) and j < len(sortright):
        if sortleft[i] < sortright[j]:
            result.append(sortleft[i])
            i += 1
        else:
            result.append(sortright[j])
            j += 1
    result.extend(sortleft[i:])
    result.extend(sortright[j:])

    return result


my_array = [15, 1, 16, 14, 12, 60, 50, 55]
mergesort(my_array)
print("Sorted array:", my_array)


