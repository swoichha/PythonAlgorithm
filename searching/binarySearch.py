def binarySearch(array, item, left, right):
    """
    Takes sorted array, item to search, leftmost index and the right most index as input
    """
    mid = left + (right - left) // 2
    if left > right:
        return -1

    if array[mid] == item:
        return mid
    elif array[mid] > item:
        return binarySearch(array, item, left, mid - 1)
    else:
        return binarySearch(array, item, mid + 1, right)